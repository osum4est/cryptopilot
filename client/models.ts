interface Currency {
    readonly url: string;
    readonly currencyId: string;
    readonly baseCurrency: string;
    readonly quoteCurrency: string;
    readonly name: string;
}

interface CurrencyData {
    readonly currency: Currency;
    readonly currencyId: string;
    readonly startDate: Date;
    readonly endDate: Date;
    readonly minPrice: number;
    readonly maxPrice: number;
}
