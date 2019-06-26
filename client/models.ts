import _ from 'lodash';

export interface Currency {
    url: string;
    currencyId: string;
    baseCurrency: string;
    quoteCurrency: string;
    name: string;
}

export function Currency(json: any): Currency {
    return toCamelCase(json) as Currency;
}

export interface CurrencyData {
    currency: Currency;
    currencyId: string;
    startDate: Date;
    endDate: Date;
    minPrice: number;
    maxPrice: number;
}

export function CurrencyData(json: any): CurrencyData {
    return toCamelCase(json) as CurrencyData;
}

function toCamelCase(json: any): any {
    return _.mapKeys(json, (v, k) => _.camelCase(k));
}
