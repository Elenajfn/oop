from abc import ABC, abstractmethod


# 1. The Interface (The Blueprint)
class PaymentProcessor(ABC):
    def __init__(self):
        # validate() stores the reason here when the details are not valid
        self.error = ""

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        pass


# 2. Concrete Implementations
class CreditCardProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        card_number = details.get("card_number")
        cvv = details.get("cvv")
        if not card_number or len(card_number) != 16:
            self.error = "Invalid card number"
            return False
        if not cvv or len(cvv) != 3:
            self.error = "Invalid CVV"
            return False
        return True

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": self.error}
        fee = amount * 0.029  # 2.9% fee
        total = amount + fee
        return {"success": True, "method": "credit_card", "amount": total, "fee": fee}


class BankTransferProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        iban = details.get("iban")
        if not iban or len(iban) < 15:
            self.error = "Invalid IBAN"
            return False
        return True

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": self.error}
        fee = 1.50  # flat fee
        total = amount + fee
        return {"success": True, "method": "bank_transfer", "amount": total, "fee": fee}


class PayPalProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        email = details.get("email")
        if not email or "@" not in email:
            self.error = "Invalid PayPal email"
            return False
        return True

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": self.error}
        fee = amount * 0.034 + 0.30  # 3.4% + 0.30 euro
        total = amount + fee
        return {"success": True, "method": "paypal", "amount": total, "fee": fee}


# 3. The Factory
class PaymentFactory:
    def __init__(self):
        self._processors = {
            "credit_card": CreditCardProcessor,
            "bank_transfer": BankTransferProcessor,
            "paypal": PayPalProcessor,
        }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_type)
        if processor_class is None:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

    # adding a new payment method = one new class + one call to register
    # (the existing code is never modified: Open/Closed principle)
    def register(self, payment_type: str, processor_class) -> None:
        self._processors[payment_type] = processor_class


# Same function name as the legacy code, now only 5 lines
def process_payment(payment_type: str, amount: float, details: dict) -> dict:
    try:
        processor = PaymentFactory().get_processor(payment_type)
    except ValueError as error:
        return {"success": False, "error": str(error)}
    return processor.process(amount, details)


if __name__ == "__main__":
    factory = PaymentFactory()

    processor = factory.get_processor("credit_card")
    print(processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"}))

    processor = factory.get_processor("bank_transfer")
    print(processor.process(100.0, {"iban": "FR7630006000011234567890189"}))

    processor = factory.get_processor("paypal")
    print(processor.process(100.0, {"email": "me@example.com"}))

    # invalid details and unknown type
    print(factory.get_processor("credit_card").process(100.0, {"card_number": "123"}))
    print(process_payment("bitcoin", 100.0, {}))
