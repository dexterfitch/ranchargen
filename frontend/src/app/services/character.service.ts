import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

interface Palette {
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

@Injectable({
  providedIn: 'root'
})
export class CharacterService {
  private baseUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  getRandomCharacter(): Observable<Character> {
    return this.http.get<Character>(`${this.baseUrl}/character`);
  }

  getRecentCharacters(): Observable<Character[]> {
    return this.http.get<Character[]>(`${this.baseUrl}/recent`);
  }

  getExampleCharacters(): Observable<Character[]> {
    return this.http.get<Character[]>(`${this.baseUrl}/example`);
  }

  saveCharacter(character: Character): Observable<any> {
    return this.http.post(`${this.baseUrl}/character`, character);
  }
}