import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Character } from '../../models/character.model';
import { CharacterService } from '../../services/character.service';
import { CharacterCardComponent } from '../../components/character-card/character-card.component';
import { RecentCharactersComponent } from '../../components/recent-characters/recent-characters.component';

@Component({
  standalone: true,
  imports: [CommonModule, CharacterCardComponent, RecentCharactersComponent],
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  character: Character | null = null;
  recentRefreshToken = 0;

  @Output() errorChange = new EventEmitter<string>();
  @Output() loadingChange = new EventEmitter<boolean>();

  constructor(private characterService: CharacterService) {}

  ngOnInit(): void {
    this.getCharacter();
  }

  getCharacter(): void {
    this.loadingChange.emit(true);

    this.characterService.getRandomCharacter().subscribe({
      next: (data) => {
        this.character = data;
        this.recentRefreshToken++;
        this.errorChange.emit('');
        this.loadingChange.emit(false);
      },
      error: (err) => {
        console.error(err);
        this.errorChange.emit('Failed to load character data.');
        this.loadingChange.emit(false);
      }
    });
  }
}