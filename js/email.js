function SendEmail(FromEmail, Message) {

   

    $.ajax({
        url: "http://eaoemail.appspot.com/?FromEmail=" + FromEmail + "&Message=" + Message
    })

}