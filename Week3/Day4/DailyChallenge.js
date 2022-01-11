/* TASK: Not Bad

    1. Create a variable called sentence. The value of the variable should be a string that
        contains the words "not" and "bad". For example, "The movie is not that bad, I like it".
    2. Create a variable called wordNot where it's value is the first appearance of the substring9
        "not" (from the sentence variable).
    3. Create a variable called wordBad where it's value is the first appearance of the substring
        "bad" (from the sentence variable).
    4. If the word "bad" comes after the word "not", you should replace the whole "not...bad"
        substring with "good", then console.log the result.
        For example, the result here should be: "The movie is good, I like it"
    5. If the word "bad" does not come after "not" or the words are not in the sentence,
        console.log the original sentence.
*/

let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot < wordBad && wordNot > -1 && wordBad > -1) {
    console.log(sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad+3));
} else {
    console.log(sentence);
}