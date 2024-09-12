
function setCustomValiditionMsg(name) {
    var input = document.getElementsByName(name)[0];
    if (input.value == '') {
        input.setCustomValidity('این قسمت را پر نمایید');
    } else {
        input.setCustomValidity('');
    }
}

function setEmailCustomValiditionMsg(name) {
    var input = document.getElementsByName(name)[0];
    if (input.value == '') {
        input.setCustomValidity('این قسمت را پر نمایید');
    } else if (!input.value.includes("@")) {
        input.setCustomValidity('ایمیل را صحیح وارد کنید');
    } else {
        input.setCustomValidity('');
    }
}

function checkMaxSize(name, size) {
    var input = document.getElementsByName(name)[0];
    console.log(name, size)
    if (input.value.length > size) {
        return ("اندازه" + " " + convertLabelToFa[name] + " " + "بیش از حد وارد شده است.") + "<br>"
    } else {
        return ""
    }
}
function checkMinSize(name, size) {
    var input = document.getElementsByName(name)[0];
    if (input.value.length < size) {
        return ("اندازه" + " " + convertLabelToFa[name] + " " + "حداقل باید " + size.toString() + " رقم باشد.") + "<br>"
    } else {
        return ""
    }
}

function getErrorRegistrationAndNationalPinIfTypeWasCompany() {
    var message = ""
    var typeInput = document.getElementsByName("type")[0];
    if (typeInput.value == 2) {
        var nationValue = document.getElementsByName("nation_code")[0].value;
        var nationalPinValue = document.getElementsByName("national_pin")[0].value;
        var registrationValue = document.getElementsByName("registration_no")[0].value;
        if (nationalPinValue == "") {
            message += "شناسه اقتصادی نمی تواند خالی باشد" + "<br>"
        }
        if (registrationValue == "") {
            message += "شماره ثبت نمی تواند خالی باشد" + "<br>"
        }
        if (nationValue != "" && nationalPinValue != "" && nationValue != nationalPinValue) {
            message += "در حال حاضر سامانه، صورتحساب هایی که شناسه ملی و کد اقتصادی یکسانی نداشته باشند را قبول نخواهد کرد. لطفا مقدار کد اقتصادی را شناسه ملی قرار دهید" + "<br>"
        }
    }
    return message
}