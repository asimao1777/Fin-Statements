import openpyxl


class FS:

    def __init__(self, company: str, mes: str, ano: int) -> object:
        """
        Initialize new Financial Statement object for a
        Company in a specific Month and Year.

        :param company: a Python String (name of the Company)
        :param mes: a Python String (name of the Month of the Financial Statements)
        :param ano: am Integer (Year of the financial statements)

        :return: does not return
        """
        self._company = company
        self._mes = mes
        self._ano = ano
        self._bs = {
                    1:    "Assets",
                    11:   "Current Assets",
                    1100: "Cash & Cash Equivalents",
                    1101: "Inventories",
                    1102: "Trade & Other Receivables",
                    1103: "Loans & Receivables (ST)",
                    1104: "Inter-company Loan Receivables (ST)",
                    1105: "Recoverable Taxes (ST)",
                    1106: "Prepayments",
                    1107: "Other Current Assets",
                    12:   "Non-Current Assets",
                    1200: "Escrow Deposits",
                    1201: "Available for Sale Assets",
                    1202: "Judicial Deposits",
                    1203: "Recoverable Taxes (LT)",
                    1204: "Deferred Tax Assets",
                    1205: "Loans & Receivables (LT)",
                    1206: "Inter-company Loan Receivables (LT)",
                    1207: "Investment in Associates",
                    1208: "Goodwill in Associates",
                    1209: "Property, Plant & Equipment",
                    1210: "Mining Rights & Properties",
                    1211: "Exploration Costs",
                    1212: "Development Costs",
                    1213: "Other Intangible Assets",
                    1214: "Other Non-Current Assets",

                    2:    "Liabilities & Shareholders' Equity",
                    21:   "Current Liabilities",
                    2100: "Trade & Other Payable",
                    2101: "Taxes Payable (ST)",
                    2102: "Payroll & Social Security Charges",
                    2103: "Advances from Clients (ST)",
                    2104: "Accrued Short Term Payable",
                    2105: "Investors Option Derivative (ST)",
                    2106: "Loans & Financing (ST)",
                    2107: "Inter-company Loan Payable (ST)",
                    2108: "Debentures (ST)",
                    2109: "Royalties Payable (ST)",
                    2110: "Dividends Payable (ST)",
                    2111: "Other Current Liabilities",
                    22:   "Non-Current Liabilities",
                    2200: "Accrued Long Term Payable",
                    2201: "Contingencies",
                    2202: "Taxes Payable (LT)",
                    2203: "Advances from Clients (LT)",
                    2204: "Investors Option Derivative (LT)",
                    2205: "Debentures (LT)",
                    2206: "Royalties Payable (LT)",
                    2207: "Rehabilitation Costs",
                    2208: "Loans & Financing (LT)",
                    2209: "Inter-company Loan Payable (LT)",
                    2210: "Deferred Tax Liabilities",
                    2211: "Minority Interests",
                    2212: "Other Non-Current Liabilities",
                    23:   "Equity Attributable to Equity Holders of the Parent",
                    2300: "Paid In Capital",
                    2301: "Unpaid Share Capital",
                    2302: "Share Premium Account",
                    2303: "Share Option Reserve",
                    2304: "Other Reserves",
                    2305: "Profit & Loss for the Period/Year",
                    2306: "Retained Earnings (Losses)",
                    2307: "Cumulative Translation Adjustments"
                   }

        self._dre = {
                     4:    "Sales Revenues",
                     4000: "Gross Revenues",
                     4001: "Taxes on Sales",
                     4002: "Discounts & Rebates",
                     4003: "Royalties",
                     4004: "Net Revenues",

                     3:    "Production Costs",
                     3000: "Cost of Goods Sold",

                     5:    "Gross Profit (Loss)",
                     5000: "Gross Profit(Loss)",
                     5001: "Logistics, Storage & Handling Expenses",
                     5002: "Commissions on Sales",
                     5003: "Gross Profit (Loss) after Logistics & Commissions Expenses",
                     5998: "Gross Margin (%)",
                     5999: "Gross Margin after Logistics & Commissions Expenses (%)",

                     6:    "Operational Expenses",
                     6000: "Sales Expenses",
                     6100: "General & Administrative Expenses",
                     6101: "Other Operational Expenses",
                     6102: "Operational Expenses",
                     6103: "G&A/Net Revenues (%)",

                     7:    "Underlying EBITDA",
                     7000: "Underlying EBITDA",
                     7001: "Underlying EBITDA/Net Revenues (%)",

                     8:    "EBITDA",
                     8001: "Non Recurring Income (Expenses)",
                     8002: "Restructuring Expenses",
                     8003: "Fundraising Expenses",
                     8004: "Bonuses Paid",
                     8005: "Inventories NRV Accrual",
                     8006: "Other Provisions",
                     8007: "EBITDA",
                     8008: "EBITDA Margin (%)",

                     9:    "Net Profit (Loss)",
                     9000: "Depreciation, Amortization & Exhaustion",
                     9001: "EBIT",
                     9002: "EBIT Margin (%)",
                     9003: "Interest Expenses",
                     9004: "Interest Income (Other than Equity)",
                     9005: "Tax Expenses (Other than Corporate Income Taxes)",
                     9006: "Result from Equity",
                     9007: "Gain (Loss) on Translation",
                     9008: "Profit & Loss Before Income Taxes",
                     9009: "Income Taxes",
                     9010: "Net Profit (Loss)",
                     9011: "Net Margin (%)"
                    }

        self._cf = {
                    "A000": "Adjustments to Reconcile Net Profit (Loss) to Net Cashflows",
                    "A001": "Non Recurring Income (Expenses)",                                      # 8001
                    "A002": "Bonuses Paid",                                                         # 8004
                    "A003": "Inventories NRV Accrual",                                              # 8005
                    "A004": "Other Provisions",                                                     # 8006
                    "A005": "Depreciation, Amortization & Exhaustion",                              # 9000
                    "A006": "Interest Expenses",                                                    # 9003
                    "A007": "Interest Income (Other than Equity)",                                  # 9004
                    "A008": "Tax Expenses (Other than Corporate Income Taxes)",                     # 9005
                    "A009": "Result from Equity",                                                   # 9006
                    "A010": "Gain (Loss) on Translation",                                           # 9007

                    "B000": "Need of Working Capital Variation",
                    "B001": "Net Cash Outflow from Operating Activities",
                    "B002": "Decrease (Increase) in Trade and Other Receivables",
                    "B003": "Decrease (Increase) in Inventories",
                    "B004": "Decrease (Increase) in Non-Current Assets",
                    "B005": "Increase (Decrease) in Other Tax Liabilities",
                    "B006": "Increase (Decrease) in Trade & Other Payable",
                    "B007": "Increase (Decrease) in Non-Current Liabilities",
                    "B008": "Other",

                    "C000": "Net Cash Outflow from Investing Activities",
                    "C001": "Mining Rights & Properties",
                    "C002": "Investment in Subsidiaries",
                    "C003": "Exploration Expenditures Incurred",
                    "C004": "Development Costs Incurred",
                    "C005": "Purchase (Sale) of Property, Plant & Equipment",
                    "C006": "Purchase (Sale) of Intangible Assets other than Exploration Costs",

                    "D000": "Net Cash Inflow from Financing Activities",
                    "D001": "Interest Income (Other than Equity)",                                  # A007, 9004
                    "D002": "Loans & Financing",
                    "D003": "Proceeds from Issuance of Shares",
                    "D004": "Cost of Shares Issued",
                    "D005": "Increase (Decrease) of Tax Financing",

                    "E000": "Net Increase in Cash & Cash Equivalents",
                    "E001": "Other Financial Movements",

                    "F000": "Cash & Cash Equivalents at the Beginning of Period",
                    "F001": "Foreign Exchange Variation on Cash",
                    "F002": "Cash & Cash Equivalents at the End of Period"
                   }

        self._param_nbe = {
            101010208:,
            101010209:,
            101010210:,
            101010401:,
            101010501:,
            101010502:,
            101010503:,
            101010504:,
            101010505:,
            101020101:,
            101020102:,
            101020103:,
            101030101:,
            101030102:,
            101070101:,
            102040101:,
            102040102:,
            102040103:,
            102040202:,
            102040301:,
            102040401:,
            102050101:,
            102060201:,
            102060202:,
            102060301:,
            102070101:,
            201010101:,
            201010201:,
            201010301:,
            201010401:,
            201010402:,
            201010403:,
            201011001:,
            201011002:,
            201011201:,
            201011202:,
            201011501:,
            201011502:,
            202010101:,
            202010102:,
            202010103:,
            202010201:,
            202010202:,
            202010203:,
            202010601:,
            203010101:,
            203010102:,
            203010103:,
            203010104:,
            203010105:,
            203030101:,
            401010101:,
            401010102:,
            401010103:,
            401010104:,
            401010105:,
            401010201:,
            401010301:,
            401010302:,
            401010303:,
            401010304:,
            401010305:,
            401010306:,
            401010401:,
            401010402:,
            401010501:,
            401010502:,
            401010601:,
            401010701:,
            401010702:,
            401010703:,
            401010801:,
            401010802:,
            401010803:,
            401010804:,
            401010805:,
            401010806:,
            401010807:,
            401010808:,
            401010901:,
            401010902:,
            401010903:,
            401010904:,
            401011001:,
            401011002:,
            401011003:,
            401011004:,
            401011005:,
            401011006:,
            401011007:,
            401011008:,
            401011009:,
            401011010:,
            401011011:,
            401011012:,
            401011201:,
            401011202:,
            401011203:,
            401011301:,
            401011401:,
            401011402:,
            401011403:,
            401011404:,
            401011405:,
            401011601:,
            401011602:,
            401011603:,
            401011604:,
            401011605:,
            401011606:,
            401020101:,
            401020201:,
            401020202:,
            401020203:,
            401020204:,
            401020301:,
            501010101:,

        }

    def __str__(self) -> str:
        """
        Override string method to provide more readable output.

        :param: any attribute of a FS object

        :return: a Python string
        """
        return (f"Empresa: {self._company}\n"
                f"Período: {self._mes} / {self._ano}")

    def get_company(self):
        return self._company

    def get_mes(self):
        return self._mes

    def get_ano(self):
        return self._ano

    def get_bs(self):
        return self._bs

    def get_dre(self):
        return self._dre

    def get_cf(self):
        return self._cf

    def set_company(self, new_company):
        self._company = new_company

    def set_mes(self, new_mes):
        self._mes = new_mes

    def set_ano(self, new_ano):
        self._ano = new_ano


novo = FS("BRN", "Janeiro", 2024)
print(novo)



# wb = openpyxl.load_workbook("")