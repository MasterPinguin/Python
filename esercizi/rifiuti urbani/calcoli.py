import costanti

def calcola_imponibile(numero_persone):
    tariffa_base = costanti.TARIFFA_BASE
    raccolta_presunta = numero_persone * costanti.LITRI_PER_PERSONA_ANNUALI
    tariffa_raccolta = costanti.TARIFFA_RACCOLTA
    return tariffa_base + (raccolta_presunta * tariffa_raccolta)

def calcola_iva(imponibile):
    aliquota_iva = costanti.ALIQUOTA_IVA
    return imponibile * aliquota_iva
