from enum import Enum


# All known and usable Categories of transactions. The top of each section is intended as a super-set of lower enums.
#  For Example, BILLS_AND_UTILITIES encompasses HOME_PHONE through UTILITIES as they are all recurring bills.
#  This relationship is modeled in the database as a node-parent relationship
class Category(Enum):
    AUTO_AND_TRANSPORT = 'Auto & Transport'
    AUTO_INSURANCE = 'Auto Insurance'
    AUTO_PAYMENT = 'Auto Payment'
    GAS_AND_FUEL = 'Gas & Fuel'
    PARKING = 'Parking'
    PUBLIC_TRANSPORTATION = 'Public Transportation'
    RIDE_SHARE = 'Ride Share'
    SERVICE_AND_PARTS = 'Service & Parts'
    TICKETS_AND_FINES = 'Tickets & Fines'

    BILLS_AND_UTILITIES = 'Bills & Utilities'
    HOME_PHONE = 'Home Phone'
    INTERNET = 'Internet'
    MOBILE_PHONE = 'Mobile Phone'
    TELEVISION = 'Television'
    UTILITIES = 'Utilities'

    BUSINESS_SERVICES = 'Business Services'
    ADVERTISING = 'Advertising'
    LEGAL = 'Legal'
    OFFICE_SUPPLIES = 'Office Supplies'
    PRINTING = 'Printing'
    SHIPPING = 'Shipping'

    EDUCATION = 'Education'
    BOOKS_AND_SUPPLIES = 'Books & Supplies'
    STUDENT_LOAN = 'Student Loan'
    TUITION = 'Tuition'

    ENTERTAINMENT = 'Entertainment'
    AMUSEMENT = 'Amusement'
    ARTS = 'Arts'
    MOVIES_AND_DVDS = 'Movies & DVDs'
    MUSIC = 'Music'
    NEWSPAPERS_AND_MAGAZINES = 'Newspapers & Magazines'

    FEES_AND_CHARGES = 'Fees & Charges'
    ATM_FEE = 'ATM Fee'
    BANK_FEE = 'Bank Fee'
    FINANCE_CHARGE = 'Finance Charge'
    LATE_FEE = 'Late Fee'
    SERVICE_FEE = 'Service Fee'
    TRADE_COMMISSIONS = 'Trade Commissions'

    FINANCIAL = 'Financial'
    FINANCIAL_ADVISOR = 'Financial Advisor'
    LIFE_INSURANCE = 'Life Insurance'

    FOOD_AND_DINING = 'Food & Dining'
    ALCOHOL_AND_BARS = 'Alcohol & Bars'
    COFFEE_SHOPS = 'Coffee Shops'
    FAST_FOOD = 'Fast Food'
    FOOD_DELIVERY = 'Food Delivery'
    GROCERIES = 'Groceries'
    HELLO_FRESH = 'Hello Fresh'
    RESTAURANTS = 'Restaurants'

    GIFTS_AND_DONATIONS = 'Gifts & Donations'
    CHARITY = 'Charity'
    GIFT = 'Gift'

    HEALTH_AND_FITNESS = 'Health & Fitness'
    DENTIST = 'Dentist'
    DOCTOR = 'Doctor'
    EYECARE = 'Eyecare'
    GYM = 'Gym'
    HEALTH_INSURANCE = 'Health Insurance'
    PHARMACY = 'Pharmacy'
    SPORTS = 'Sports'

    HIDE_FROM_BUDGETS_AND_TRENDS = 'Hide from Budgets & Trends'

    HOME = 'Home'
    FURNISHINGS = 'Furnishings'
    HOME_IMPROVEMENT = 'Home Improvement'
    HOME_INSURANCE = 'Home Insurance'
    HOME_OWNERS_ASSOC = 'Home Owners Assoc'
    HOME_SERVICES = 'Home Services'
    HOME_SUPPLIES = 'Home Supplies'
    LAWN_AND_GARDEN = 'Lawn & Garden'
    MORTGAGE_AND_RENT = 'Mortgage & Rent'

    INCOME = 'Income'
    BONUS = 'Bonus'
    INTEREST_INCOME = 'Interest Income'
    PAYCHECK = 'Paycheck'
    REIMBURSEMENT = 'Reimbursement'
    RENTAL_INCOME = 'Rental Income'
    RETURNED_PURCHASE = 'Returned Purchase'
    TAX_RETURN = 'Tax Return'

    INVESTMENTS = 'Investments'
    BUY = 'Buy'
    DEPOSIT = 'Deposit'
    DIVIDEND_AND_CAP_GAINS = 'Dividend & Cap Gains'
    SELL = 'Sell'
    WITHDRAWAL = 'Withdrawal'

    KIDS = 'Kids'
    ALLOWANCE = 'Allowance'
    BABY_SUPPLIES = 'Baby Supplies'
    BABYSITTER_AND_DAYCARE = 'Babysitter & Daycare'
    CHILD_SUPPORT = 'Child Support'
    COLLEGE_FUND = 'College Fund'
    KIDS_ACTIVITIES = 'Kids Activities'
    TOYS = 'Toys'

    LOANS = 'Loans'
    LOAN_FEES_AND_CHARGES = 'Loan Fees and Charges'
    LOAN_INSURANCE = 'Loan Insurance'
    LOAN_INTEREST = 'Loan Interest'
    LOAN_PAYMENT = 'Loan Payment'
    LOAN_PRINCIPAL = 'Loan Principal'

    MISC_EXPENSES = 'Misc Expenses'

    PERSONAL_CARE = 'Personal Care'
    HAIR = 'Hair'
    LAUNDRY = 'Laundry'
    SPA_AND_MASSAGE = 'Spa & Massage'

    PETS = 'Pets'
    PET_FOOD_AND_SUPPLIES = 'Pet Food & Supplies'
    PET_GROOMING = 'Pet Grooming'
    VETERINARY = 'Veterinary'

    SHOPPING = 'Shopping'
    BOOKS = 'Books'
    CLOTHING = 'Clothing'
    ELECTRONICS_AND_SOFTWARE = 'Electronics & Software'
    HOBBIES = 'Hobbies'
    SPORTING_GOODS = 'Sporting Goods'

    TAXES = 'Taxes'
    FEDERAL_TAX = 'Federal Tax'
    LOCAL_TAX = 'Local Tax'
    PROPERTY_TAX = 'Property Tax'
    SALES_TAX = 'Sales Tax'
    STATE_TAX = 'State Tax'

    TRANSFER = 'Transfer'
    CREDIT_CARD_PAYMENT = 'Credit Card Payment'
    TRANSFER_FOR_CASH_SPENDING = 'Transfer for Cash Spending'

    TRAVEL = 'Travel'
    AIR_TRAVEL = 'Air Travel'
    HOTEL = 'Hotel'
    RENTAL_CAR_AND_TAXI = 'Rental Car & Taxi'
    VACATION = 'Vacation'

    UNCATEGORIZED = 'Uncategorized'
    CASH_AND_ATM = 'Cash & ATM'
    CHECK = 'Check'
    SOLAR_LOAN = 'Solar Loan'

    UNKNOWN = "Unknown"
