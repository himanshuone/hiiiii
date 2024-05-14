from django.shortcuts import render, redirect
from .models import Donor, DonationCause, BlogPost, ContactForm, Sponsor, Service, RescueRequest



def index(request):
    donation_causes = DonationCause.objects.all().order_by('-id')  # Fetch all causes, order by descending ID
    sliced_causes = donation_causes[:3] 
    latest_posts = BlogPost.objects.order_by('-pub_date')[:3]
    donors = Donor.objects.all()
    sponsors = Sponsor.objects.all() 
    services = Service.objects.all()
    if request.method == 'POST':
        # Form submission handling
        if 'form' in request.POST:  # Using a form (optional)
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  # Save form data to database
                # Success message or redirect (logic here)
                return redirect('success_url')  # Replace with your success URL
        else:  # Handling raw form data (without form class)
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            purpose = request.POST['purpose']
            event_name = request.POST.get('event_name', '')  # Get event_name (optional)
            contact_form = ContactForm.objects.create(
                name=name, email=email, message=message, purpose=purpose, event_name=event_name
            )
            # Success message or redirect (logic here)
            return redirect('index')  # Replace with your success URL
    else:
        # Display the form
        if 'form' in request.GET:  # Using a form (optional)
            form = ContactForm()
        else:
            form = None  # No form object needed
    context = {
        # 'donation_causes': donation_causes,
        'latest_posts': latest_posts,
        'donation_causes': sliced_causes,
        'donors': donors,
        'sponsors': sponsors,
        'form': form,
        'services': services,
    }
    return render(request, "index.html", context)



def view_responses(request):
    all_responses = ContactForm.objects.all().order_by('-id')  # Get all responses (ordered by descending ID)
    context = {'responses': all_responses}
    return render(request, 'view_responses.html', context)


def index2(request):
    return render(request, "index-2.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def event(request):
    return render(request, "event.html")
def gallery(request):
    return render(request, "gallery.html")
def blogs(request):
    return render(request, "blog-single.html")
def rescue(request):
      if request.method == 'POST':
        category = request.POST.get('category')
        location = request.POST.get('location')
        details = request.POST.get('details')

        # Validate data (optional, you can add more sophisticated validation)
        if not category or not location or not details:
            # Display an error message in the context
            context = {'error': 'Please fill out all required fields.'}
            return render(request, 'rescue.html', context)

        # Create a new rescue request object
        rescue_request = RescueRequest.objects.create(
            category=category,
            location=location,
            details=details
        )

        # Handle success (redirect or display message)
        return render(request, 'rescue.html', {'success': 'Thank you for submitting a rescue request!'})

      return render(request, 'rescue.html')
def certificate(request):
    return render(request, "certificate.html")
def rescue(request):
    return render(request, "rescue.html")

