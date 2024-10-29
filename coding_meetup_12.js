function findAdmin(list, lang) {
 return list.filter(dev=>{if(dev.language===lang&&dev.githubAdmin==="yes")return dev})
}