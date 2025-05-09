import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CharacterCardComponent } from '../character-card/character-card.component';
import { Character } from '../../models/character.model';
import { CharacterService } from '../../services/character.service';

@Component({
  selector: 'app-recent-characters',
  standalone: true,
  imports: [CommonModule, CharacterCardComponent],
  templateUrl: './recent-characters.component.html',
  styleUrls: ['./recent-characters.component.scss']
})
export class RecentCharactersComponent implements OnInit {
  recentCharacters: Character[] = [];
  loading = false;
  error: string = '';

  constructor(private characterService: CharacterService) {}

  ngOnInit(): void {
    this.getRecentCharacters();
  }

  getRecentCharacters(): void {
    this.loading = true;
    this.characterService.getRecentCharacters().subscribe({
      next: (data) => {
        this.recentCharacters = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'Failed to load recent characters.';
        this.loading = false;
      }
    });
  }
}
