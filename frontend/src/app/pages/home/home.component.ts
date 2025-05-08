import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from '../../components/header/header.component';
import { Character } from '../../models/character.model';
import { CharacterService } from '../../services/character.service';
import { CharacterCardComponent } from '../../components/character-card/character-card.component';

@Component({
  standalone: true,
  imports: [CommonModule, HeaderComponent, CharacterCardComponent],
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
