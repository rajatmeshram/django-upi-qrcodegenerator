from django.shortcuts import render
from django.conf import settings
import qrcode
import os

def index(request):
    return render(request, "index.html")

def generate(request):
    if request.method == "POST":
        upi_id = settings.UPI_ID
        method = request.POST.get("method")

        if method == "google":
            pay_url = f"upi://pay?pa={upi_id}&pn=GooglePay&mc=0000"
        elif method == "phonepe":
            pay_url = f"upi://pay?pa={upi_id}&pn=PhonePe&mc=0000"
        else:
            pay_url = f"upi://pay?pa={upi_id}&pn=Paytm&mc=0000"

        # ⭐ Correct Absolute Path
        qr_path = os.path.join(settings.BASE_DIR, "pay", "static", "qr.png")

        # Create directory if missing
        os.makedirs(os.path.dirname(qr_path), exist_ok=True)

        img = qrcode.make(pay_url)
        img.save(qr_path)

        return render(request, "success.html")

    return render(request, "index.html")

def done(request):
    return render(request, "thanks.html")
