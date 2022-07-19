from dataclasses import dataclass

@dataclass(frozen=True)
class JPCorporateAddressPage:
    name : str = ''
    address : str = ''
