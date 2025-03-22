from django.core.validators import RegexValidator

phone_validators = RegexValidator(
    regex=r"^\+?1?\d{9,15}$", message="15 tadan son kam bolishi kerak...  Standart raqam talab qilinadi"
)
