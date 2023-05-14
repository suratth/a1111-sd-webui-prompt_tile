function cardClicked_plus(tabname, textToAdd, TextToAddNeg){

    var textarea_pro = gradioApp().querySelector("#" + tabname + "_prompt > label > textarea")
    var textarea_neg = gradioApp().querySelector("#" + tabname + "_neg_prompt > label > textarea")

    if(! tryToRemoveExtraNetworkFromPrompt_plus(textarea_pro, textToAdd)){
        textarea_pro.value = textarea_pro.value + opts.extra_networks_add_text_separator + textToAdd
    }
    
    if(! tryToRemoveExtraNetworkFromPrompt_plus(textarea_neg, TextToAddNeg)){
        textarea_neg.value = textarea_neg.value + opts.extra_networks_add_text_separator + TextToAddNeg
    }

    updateInput(textarea_pro)
    updateInput(textarea_neg)
}


function tryToRemoveExtraNetworkFromPrompt_plus(textarea, text){

    // textareaの値を取得し、正規化します（改行や空白を除去）
    var textareaValue = textarea.value.replace(/[\n\s]/g, '');

    // textが空文字列の場合は除去の必要がないため、falseを返します
    if (text === '') {
        return false;
    }

    // textareaValueからtextを除去します
    var updatedValue = textareaValue.replace(text, '');

    // 更新後の値が元の値と異なる場合は除去が行われたことを意味します
    if (updatedValue !== textareaValue) {
        textarea.value = updatedValue;
        return true;
    }

    // 除去が行われなかった場合はfalseを返します
    return false;
}