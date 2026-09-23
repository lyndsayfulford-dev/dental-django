from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        # Fixed syntax: changed square brackets [] to parentheses ()
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')

        try:
            # Fixed arguments to match standard Django send_mail parameters
            send_mail(
                subject=f'New Dental Contact from {message_name}', 
                message=message, 
                from_email=message_email, 
                recipient_list=['admind@gmail.com'], 
                fail_silently=False,
            )
            
            # Send the template back with the success message variable included
            return render(request, 'contact.html', {'message_name': message_name})

        except Exception as e:
            # Print the actual system error to your terminal for tracking
            print(f"Email failed to send: {e}")
            return render(request, 'contact.html', {'error': 'Failed to send message.'})

    # If it is a GET request (initial page load), just render a clean contact page
    return render(request, 'contact.html', {})