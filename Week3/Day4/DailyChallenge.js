let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot < wordBad && wordNot > -1 && wordBad > -1) {
    console.log(sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad+3));
} else {
    console.log(sentence);
}