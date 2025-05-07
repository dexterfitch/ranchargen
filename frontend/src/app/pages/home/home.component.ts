import { Component, OnInit } from '@angular/core';
import { Character, CharacterService } from '../../services/character.service';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  character: Character | null = null;
  loading = false;
  error: string = '';

  constructor(private characterService: CharacterService) {}

  ngOnInit(): void {
    this.getCharacter();
  }

  getCharacter(): void {
    this.loading = true;
    this.characterService.getRandomCharacter().subscribe({
      next: (data) => {
        this.character = data;
        this.error = '';
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to load character data.';
        this.loading = false;
      }
    });
  }
}
