const resumeFieldlist = [
    "name", "home_phone_no", "fax_no", "phone_no"
    , "nation_code", "national_pin", "registration_no", "postal_code_no", "province", "city"
]
const resumeFieldlist_limitsize = [
    150, 13, 13, 13, 12, 14, 6, 10, 30, 30
]

const resumeConvertLabelToFa = {
    "type": "نوع مشتری",
    "name": "نام و نام خانوادگی",
    "home_phone_no": "شماره تلفن",
    "fax_no": "شماره فکس",
    "phone_no": "شماره تلفن همراه",
    "nation_code": "شناسه ملی",
    "national_pin": "شماره اقتصادی",
    "registration_no": "شماره ثبت",
    "postal_code_no": "کدپستی",
    "province": "استان",
    "city": "شهر",
    "address": "آدرس",
};

$('#btn-create-resume-form').on('click', function (event) {
    //set custom validation message
    setCustomValiditionMsg("type")
    setCustomValiditionMsg("name")
    // setEmailCustomValiditionMsg("email")
    // setCustomValiditionMsg("home_phone_no")
    // setCustomValiditionMsg("fax_no")
    // setCustomValiditionMsg("phone_no")
    // setCustomValiditionMsg("nation_code")
    // setCustomValiditionMsg("national_pin")
    // setCustomValiditionMsg("registration_no")
});

function checkresumeValidation(event) {
    var message = '';
    var error_count = 0;
    for (let i = 0; i < resumeFieldlist.length; i++) {
        error = checkFormMaxSize(resumeFieldlist[i], resumeFieldlist_limitsize[i])
        if (error != "") {
            message += ((message != "") ? ("<br>" + error) : error);
            error_count += 1;
        }
    }

    // check for national code and nationpin number to be nessecery in 
    // message += getErrorRegistrationAndNationalPinIfTypeWasCompany()

    if (message != '') {
        event.preventDefault()
        showAlert("error", error_count + " خطا", message)
        return false
    }
    return true
}

function checkFormMaxSize(name, size) {
    var input = document.getElementsByName(name)[0];
    if (input.value.length > size) {
        return ("اندازه" + " " + resumeConvertLabelToFa[name] + " " + "بیش از حد وارد شده است.")
    } else {
        return ""
    }
}

$('#create-resume-form').on('submit', function (event) {
    checkresumeValidation(event)
});

