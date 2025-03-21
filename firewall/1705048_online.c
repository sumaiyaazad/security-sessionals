#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/icmp.h>
#include <linux/if_ether.h>
#include <linux/inet.h>

int arr[6] = {0,0,0,0,0,0};


static struct nf_hook_ops hook1, hook2, hook3, hook4; 


unsigned int blockUDP(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
   struct iphdr *iph;
   struct udphdr *udph;

   u16  port   = 53;
   char ip[16] = "8.8.8.8";
   u32  ip_addr;

   if (!skb) return NF_ACCEPT;

   iph = ip_hdr(skb);
   // Convert the IPv4 address from dotted decimal to 32-bit binary
   in4_pton(ip, -1, (u8 *)&ip_addr, '\0', NULL);

   if (iph->protocol == IPPROTO_UDP) {
       udph = udp_hdr(skb);
       if (iph->daddr == ip_addr && ntohs(udph->dest) == port){
            printk(KERN_WARNING "*** Dropping %pI4 (UDP), port %d\n", &(iph->daddr), port);
            return NF_DROP;
        }
   }
   return NF_ACCEPT;
}



unsigned int blockICMP(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
   struct iphdr *iph;
   struct icmphdr *icmph;

   char ip[16] = "192.168.60.5";
   char ip1[16] = "192.168.60.6";
   char ip2[16] = "192.168.60.7";
   char ip3[16] = "192.168.60.11";
   char ip4[16] = "10.9.0.1";
   char ip5[16] = "10.9.0.5";
   char ip6[16] = "10.9.0.11";
   u32  ip_addr;
   u32 ip_addr1;
   u32 ip_addr2;
   u32 ip_addr3;
   u32 ip_addr4;
   u32 ip_addr5;
   u32 ip_addr6;
   

   if (!skb) return NF_ACCEPT;

   iph = ip_hdr(skb);
   // Convert the IPv4 address from dotted decimal to 32-bit binary
   in4_pton(ip, -1, (u8 *)&ip_addr, '\0', NULL);
   
   
   in4_pton(ip1, -1, (u8 *)&ip_addr1, '\0', NULL);
   
   
   in4_pton(ip2, -1, (u8 *)&ip_addr2, '\0', NULL);
   
   
   in4_pton(ip3, -1, (u8 *)&ip_addr3, '\0', NULL);
   
   
   in4_pton(ip4, -1, (u8 *)&ip_addr4, '\0', NULL);
   
   
   in4_pton(ip5, -1, (u8 *)&ip_addr5, '\0', NULL);
   
   
   in4_pton(ip6, -1, (u8 *)&ip_addr6, '\0', NULL);

   if (iph->protocol == IPPROTO_ICMP) {
       int flag = -1;
       icmph = icmp_hdr(skb);
       if (iph->daddr == ip_addr){
            if(iph->saddr == ip_addr1){
            	flag = 0;
            	arr[0] = arr[0] + 1;
            }
            else if(iph->saddr == ip_addr2){
            	flag = 1;
            	arr[1] = arr[1] + 1;
            }
            else if(iph->saddr == ip_addr3){
                flag = 2;
            	arr[2] = arr[2] + 1;
            }
            else if(iph->saddr == ip_addr4){
                flag = 3;
            	arr[3] = arr[3] + 1;
            }
            else if(iph->saddr == ip_addr5){
                flag = 4;
            	arr[4] = arr[4] + 1;
            }
            else if(iph->saddr == ip_addr6){
                flag = 5;
            	arr[5] = arr[5] + 1;
            }
            printk(KERN_WARNING "*** Dropping %n I4 (UDP)", &flag);
            if(flag>-1 && arr[flag]>5){
            printk(KERN_WARNING "*** Dropping dst %pI4 (UDP) src %pI4\n", &(iph->daddr),&(iph->saddr));
            	return NF_DROP;
            }else{
            	return NF_ACCEPT;
            }
        }
   }
   return NF_ACCEPT;
}

unsigned int blockTELNET(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
   struct iphdr *iph;
   struct tcphdr *tcph;

   u16  port   = 23;
   char ip[16] = "10.9.0.1";
   u32  ip_addr;

   if (!skb) return NF_ACCEPT;

   iph = ip_hdr(skb);
   // Convert the IPv4 address from dotted decimal to 32-bit binary
   in4_pton(ip, -1, (u8 *)&ip_addr, '\0', NULL);

   if (iph->protocol == IPPROTO_TCP) {
       tcph = tcp_hdr(skb);
       if (iph->daddr == ip_addr && ntohs(tcph->dest) == port){
            printk(KERN_WARNING "*** Dropping %pI4 (UDP)", &(iph->daddr));
            return NF_DROP;
        }
   }
   return NF_ACCEPT;
}

unsigned int printInfo(void *priv, struct sk_buff *skb,
                 const struct nf_hook_state *state)
{
   struct iphdr *iph;
   char *hook;
   char *protocol;

   switch (state->hook){
     case NF_INET_LOCAL_IN:     hook = "LOCAL_IN";     break; 
     case NF_INET_LOCAL_OUT:    hook = "LOCAL_OUT";    break; 
     case NF_INET_PRE_ROUTING:  hook = "PRE_ROUTING";  break; 
     case NF_INET_POST_ROUTING: hook = "POST_ROUTING"; break; 
     case NF_INET_FORWARD:      hook = "FORWARD";      break; 
     default:                   hook = "IMPOSSIBLE";   break;
   }
   printk(KERN_INFO "*** %s\n", hook); // Print out the hook info

   iph = ip_hdr(skb);
   switch (iph->protocol){
     case IPPROTO_UDP:  protocol = "UDP";   break;
     case IPPROTO_TCP:  protocol = "TCP";   break;
     case IPPROTO_ICMP: protocol = "ICMP";  break;
     default:           protocol = "OTHER"; break;

   }
   // Print out the IP addresses and protocol
   printk(KERN_INFO "    %pI4  --> %pI4 (%s)\n", 
                    &(iph->saddr), &(iph->daddr), protocol);

   return NF_ACCEPT;
}


int registerFilter(void) {
   printk(KERN_INFO "Registering filters.\n");

   hook1.hook = printInfo;
   hook1.hooknum = NF_INET_LOCAL_OUT;
   hook1.pf = PF_INET;
   hook1.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook1);

   hook2.hook = printInfo;
   hook2.hooknum = NF_INET_POST_ROUTING;
   hook2.pf = PF_INET;
   hook2.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook2);
   
   hook3.hook = printInfo;
   hook3.hooknum = NF_INET_LOCAL_IN;
   hook3.pf = PF_INET;
   hook3.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook3);
   
   hook4.hook = blockICMP;
   hook4.hooknum = NF_INET_PRE_ROUTING;
   hook4.pf = PF_INET;
   hook4.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook4);

   return 0;
}

void removeFilter(void) {
   printk(KERN_INFO "The filters are being removed.\n");
   nf_unregister_net_hook(&init_net, &hook1);
   nf_unregister_net_hook(&init_net, &hook2);
   nf_unregister_net_hook(&init_net, &hook3);
   nf_unregister_net_hook(&init_net, &hook4);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");
