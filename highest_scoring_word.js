function findKeyWithHighestValue(obj) {
    let maxKey = null;
    let maxValue = -Infinity;

    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            if (obj[key] > maxValue) {
                maxValue = obj[key];
                maxKey = key;
            }
        }
    }

    return maxKey;
}

function high(x){
    let word_li = x.split(' ')
    let alphabets_str_li = "abcdefghijklmnopqrstuvwxyz".split("")
    const current_dictionary = {}
    word_li.forEach((word)=>{
        const power = word.split('').reduce((accum,val) =>{
            return accum + (alphabets_str_li.indexOf(val) + 1)
        },0)
        current_dictionary[word] = power
    })
    console.log(current_dictionary)
    // let's find the word with the highest power 
    let highest_scoring_word = findKeyWithHighestValue(current_dictionary)
    console.log(highest_scoring_word)
    return highest_scoring_word
}