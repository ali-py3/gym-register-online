import datetime
import logging
from gym_register.models import Tuition, User
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from django.shortcuts import get_object_or_404, render


@login_required(login_url='/login')
def go_to_gateway_view(request, pk):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = Tuition.objects.get(id=pk).tiotion
    amount = int(amount)

    # print(type(amount))
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = User.objects.get(id=pk).mobile_number  # اختیار
    # user_mobile_number = str(user_mobile_number.mobile_number)

    factory = bankfactories.BankFactory()
    bank = factory.create(bank_models.BankType.IDPAY)  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url('/callback')
    bank.set_mobile_number(user_mobile_number)  # اختیاری
    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید.
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


def callback_gateway_view(request):

    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.

        return render(request, 'GYM/successful.html',{'tracking_code':tracking_code})


     # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return render(request, 'GYM/unsuccessful.html',{})
        # HttpResponse(
        # "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")

