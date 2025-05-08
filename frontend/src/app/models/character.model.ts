export interface Palette {
    name: string;
    colors: string[];
}

export interface Character {
    id?: number;
    type: string;
    occupation: string;
    style: string;
    disposition: string;
    palette: Palette;
    accessory: string;
    is_example?: boolean;
    created_at?: string;
}