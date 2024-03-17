import logging

from category import *

logger = logging.getLogger('category_inferer')


# Behold the hideous mess of category inference!
# It would be amazing if I could train a ML model to figure out what the most likely category is, but I don't have time
#  For that. Different merchants publish their names differently. Different merchants within the same brand can publish
#  their names differently as well. Python also doesn't do cascading switch statements so if/return it is.
def infer_category(text):
    text = text.lower()
    if 'airlines' in text:
        return Category.AIR_TRAVEL.value
    if 'southwest' in text:
        return Category.AIR_TRAVEL.value
    if 'american' in text:
        return Category.AIR_TRAVEL.value

    if 'liquor' in text:
        return Category.ALCOHOL_AND_BARS.value
    if 'brewing' in text:
        return Category.ALCOHOL_AND_BARS.value
    if 'sports station' in text:
        return Category.ALCOHOL_AND_BARS.value

    if 'firework' in text:
        return Category.AMUSEMENT.value
    if 'zoo' in text:
        return Category.AMUSEMENT.value

    if 'toll' in text:
        return Category.AUTO_AND_TRANSPORT.value
    if 'driver' in text:
        return Category.AUTO_AND_TRANSPORT.value
    if 'vehicle' in text:
        return Category.AUTO_AND_TRANSPORT.value

    if 'ssfcu' in text:
        return Category.AUTO_PAYMENT.value
    if 'icpayment' in text:
        return Category.AUTO_PAYMENT.value

    if 'just between friends' in text:
        return Category.BABY_SUPPLIES.value

    if 'momentpath' in text:
        return Category.BABYSITTER_AND_DAYCARE.value

    if 'overdraft' in text:
        return Category.BANK_FEE.value

    if 'barnes & noble' in text:
        return Category.BOOKS.value

    if 'Friends Of The Lvld Li' in text:
        return Category.BOOKS_AND_SUPPLIES.value

    if 'check' in text:
        return Category.CHECK.value

    if 'footwear' in text:
        return Category.CLOTHING.value
    if 'jcpenney' in text:
        return Category.CLOTHING.value

    if '529' in text:
        return Category.COLLEGE_FUND.value

    if 'cardmember' in text:
        return Category.CREDIT_CARD_PAYMENT.value

    if 'dentist' in text:
        return Category.DENTIST.value
    if 'dmd' in text:
        return Category.DENTIST.value

    if 'clinic' in text:
        return Category.DOCTOR.value
    if 'medicine' in text:
        return Category.DOCTOR.value
    if 'health' in text:
        return Category.DOCTOR.value
    if 'labcorp' in text:
        return Category.DOCTOR.value
    if 'pathology' in text:
        return Category.DOCTOR.value

    if 'test' in text:
        return Category.EDUCATION.value
    if 'exam' in text:
        return Category.EDUCATION.value
    if 'univers' in text:
        return Category.EDUCATION.value

    if 'steam' in text:
        return Category.ENTERTAINMENT.value
    if 'games' in text:
        return Category.ENTERTAINMENT.value
    if 'gog.com ' in text:
        return Category.ENTERTAINMENT.value
    if 'gog  ' in text:
        return Category.ENTERTAINMENT.value
    if 'steamgames' in text:
        return Category.ENTERTAINMENT.value
    if 'playstation' in text:
        return Category.ENTERTAINMENT.value
    if 'google' in text:
        return Category.ENTERTAINMENT.value

    if 'newegg' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value
    if 'apple' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value
    if 'jetbrains' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value
    if 'ui.com' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value
    if 'robotic' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value
    if 'home assistant cloud' in text:
        return Category.ELECTRONICS_AND_SOFTWARE.value

    if 'optical' in text:
        return Category.EYECARE.value
    if 'eye' in text: # Might be too generic
        return Category.EYECARE.value
    if 'associates in family e' in text:
        return Category.EYECARE.value

    if 'five guys' in text:
        return Category.FAST_FOOD.value
    if 'burgers' in text:
        return Category.FAST_FOOD.value
    if 'pizza' in text:
        return Category.FAST_FOOD.value
    if 'coffee' in text:
        return Category.FAST_FOOD.value
    if 'donut' in text:
        return Category.FAST_FOOD.value
    if 'starbucks' in text:
        return Category.FAST_FOOD.value
    if 'bar' in text:
        return Category.FAST_FOOD.value
    if 'cafe' in text:
        return Category.FAST_FOOD.value
    if 'grill' in text:
        return Category.FAST_FOOD.value
    if 'arby\'s' in text:
        return Category.FAST_FOOD.value
    if 'arbys' in text:
        return Category.FAST_FOOD.value
    if 'pizza' in text:
        return Category.FAST_FOOD.value
    if 'pizz' in text:
        return Category.FAST_FOOD.value
    if 'wingshack' in text:
        return Category.FAST_FOOD.value
    if 'freddys' in text:
        return Category.FAST_FOOD.value
    if 'krazy karl' in text:
        return Category.FAST_FOOD.value
    if 'good times' in text:
        return Category.FAST_FOOD.value
    if 'dominos' in text:
        return Category.FAST_FOOD.value
    if 'domino\'s' in text:
        return Category.FAST_FOOD.value
    if 'cake' in text:
        return Category.FAST_FOOD.value
    if 'dairy queen' in text:
        return Category.FAST_FOOD.value
    if 'qdoba' in text:
        return Category.FAST_FOOD.value
    if 'dairy delite' in text:
        return Category.FAST_FOOD.value
    if 'baskin ' in text:
        return Category.FAST_FOOD.value
    if 'ice cream' in text:
        return Category.FAST_FOOD.value
    if 'freeze dried' in text:
        return Category.FAST_FOOD.value

    if 'fee' in text:
        return Category.FEES_AND_CHARGES.value

    if 'honey' in text:
        return Category.FOOD_AND_DINING.value

    if 'uber eats' in text:
        return Category.FOOD_DELIVERY.value
    if 'doordash' in text:
        return Category.FOOD_DELIVERY.value
    if 'grubhub' in text:
        return Category.FOOD_DELIVERY.value

    if 'ikea' in text:
        return Category.FURNISHINGS.value
    if 'homegoods' in text:
        return Category.FURNISHINGS.value

    if 'kum&go' in text:
        return Category.GAS_AND_FUEL.value
    if 'corner store' in text:
        return Category.GAS_AND_FUEL.value
    if 'conoco' in text:
        return Category.GAS_AND_FUEL.value

    if 'sams' in text:
        return Category.GROCERIES.value
    if 'hellofresh' in text:
        return Category.GROCERIES.value
    if 'fruits' in text:
        return Category.GROCERIES.value
    if 'king soopers' in text:
        return Category.GROCERIES.value
    if 'safeway' in text:
        return Category.GROCERIES.value
    if 'grocery' in text:
        return Category.GROCERIES.value
    if 'market' in text:
        return Category.GROCERIES.value
    if 'cherry' in text:
        return Category.GROCERIES.value
    if 'sprouts' in text:
        return Category.GROCERIES.value

    if 'head zep' in text:
        return Category.HAIR.value
    if 'cookie cutters' in text:
        return Category.HAIR.value
    if 'hair' in text:
        return Category.HAIR.value

    if 'state farm' in text:
        return Category.HOME_INSURANCE.value

    if 'ace h' in text:
        return Category.HOME_IMPROVEMENT.value
    if 'home depot' in text:
        return Category.HOME_IMPROVEMENT.value
    if 'sears' in text:
        return Category.HOME_IMPROVEMENT.value
    if 'lowes' in text:
        return Category.HOME_IMPROVEMENT.value

    if 'atgpay online' in text:
        return Category.HOME_OWNERS_ASSOC.value

    if 'quality inn' in text:
        return Category.HOTEL.value

    if 'dividend' in text:
        # TODO: Not sure if this should be interest or dividend for bank interest deposits
        return Category.INTEREST_INCOME.value

    if 'pulse' in text:
        return Category.INTERNET.value
    if 'comcast' in text:
        return Category.INTERNET.value

    if 'invest' in text:
        return Category.INVESTMENTS.value

    if 'parks' in text:
        return Category.KIDS_ACTIVITIES.value

    if 'lawn' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'seed' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'landscape' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'brecks' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'seeds' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'garlic' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'kvan bourgondien ' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'garden' in text:
        return Category.LAWN_AND_GARDEN.value
    if 'nursery' in text:
        return Category.LAWN_AND_GARDEN.value

    if 'thrivent' in text:
        return Category.LIFE_INSURANCE.value

    if 'mint mobile ' in text:
        return Category.MOBILE_PHONE.value

    if 'office depot' in text:
        return Category.OFFICE_SUPPLIES.value

    if 'parking' in text:
        return Category.PARKING.value

    if 'cat' in text:
        return Category.PETS.value
    if 'dog' in text:
        return Category.PETS.value
    if 'humane society' in text:
        return Category.PETS.value

    if 'petco' in text:
        return Category.PET_FOOD_AND_SUPPLIES.value

    if 'optum' in text:
        return Category.PHARMACY.value
    if 'pharmacy' in text:
        return Category.PHARMACY.value

    if 'print' in text:
        return Category.PRINTING.value

    if 'avis.com' in text:
        return Category.RENTAL_CAR_AND_TAXI.value

    if 'noodles' in text:
        return Category.RESTAURANTS.value
    if 'olive garden' in text:
        return Category.RESTAURANTS.value
    if 'food service' in text:
        return Category.RESTAURANTS.value
    if 'texas roadhouse' in text:
        return Category.RESTAURANTS.value
    if 'pho ' in text:
        return Category.RESTAURANTS.value
    if 'wok' in text:
        return Category.RESTAURANTS.value
    if 'sala thai' in text:
        return Category.RESTAURANTS.value
    if 'santiagos mexican res' in text:
        return Category.RESTAURANTS.value
    if 'cafe mexicali' in text:
        return Category.RESTAURANTS.value
    if 'nordys' in text:
        return Category.RESTAURANTS.value
    if 'bakery' in text:
        return Category.RESTAURANTS.value
    if 'door 222' in text:
        return Category.RESTAURANTS.value
    if 'casa real' in text:
        return Category.RESTAURANTS.value
    if 'marys mountain' in text:
        return Category.RESTAURANTS.value
    if 'restaurant' in text:
        return Category.RESTAURANTS.value
    if 'mcdonald' in text:
        return Category.RESTAURANTS.value

    if 'washme cw ' in text:
        return Category.SERVICE_AND_PARTS.value
    if 'batteries+bulbs' in text:
        return Category.SERVICE_AND_PARTS.value

    if 'usps' in text:
        return Category.SHIPPING.value
    if 'us postal service' in text:
        return Category.SHIPPING.value

    if 'jax' in text:
        return Category.SHOPPING.value
    if 'rei' in text:
        return Category.SHOPPING.value
    if 'walgreens' in text:
        return Category.SHOPPING.value
    if 'amzn mktp' in text:
        return Category.SHOPPING.value
    if 'walmart' in text:
        return Category.SHOPPING.value
    if 'target' in text:
        return Category.SHOPPING.value
    if 'wal-mart' in text:
        return Category.SHOPPING.value
    if 'wm supercenter' in text:
        return Category.SHOPPING.value
    if 'amazon' in text:
        return Category.SHOPPING.value
    if 'etsy ' in text:
        return Category.SHOPPING.value
    if 'scheels' in text:
        return Category.SHOPPING.value

    if 'turbotax' in text:
        return Category.TAXES.value
    if 'taxes' in text:
        return Category.TAXES.value

    if 'bricks & minifigs' in text:
        return Category.TOYS.value

    if 'transfer' in text:
        return Category.TRANSFER.value

    if 'travel' in text:
        return Category.TRAVEL.value

    if 'city' in text:
        return Category.UTILITIES.value
    if 'xcel' in text:
        return Category.UTILITIES.value

    return Category.UNKNOWN.value
