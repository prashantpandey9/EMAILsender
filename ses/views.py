from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
def send_mail(request):
    ctx = {
        'profile': "Ajay"
    }
    message = get_template('mail.html').render(ctx)
    msg = EmailMessage(
        'Subject',
        message,
        'noreply@wiseKreator.com',
        ['prashantpandey94551@gmail.com'],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")

    return HttpResponse(f"Email sent to 1 members")
    #return HttpResponse("Email sent to "+ res +" members")