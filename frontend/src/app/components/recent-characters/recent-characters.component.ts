import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { getSmartArticle } from '../../utils/string-utils';
import { Character } from '../../models/character.model';
import { CharacterService } from '../../services/character.service';

@Component({
  selector: 'app-recent-characters',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './recent-characters.component.html',
  styleUrls: ['./recent-characters.component.scss']
})
export class RecentCharactersComponent implements OnInit, OnChanges {
  @Input() refreshTrigger: number = 0;

  recentCharacters: Character[] = [];
  loading = false;
  error: string = '';
  getArticle = getSmartArticle;

  constructor(private characterService: CharacterService) {}

  ngOnInit(): void {
    this.getRecentCharacters();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['refreshTrigger'] && !changes['refreshTrigger'].firstChange) {
      this.getRecentCharacters();
    }
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

  copyToClipboard(color: string, event: Event): void {
    const swatch = event.currentTarget as HTMLElement;
    if (!swatch) return;

    navigator.clipboard.writeText(color).catch(err => {
      console.error('Failed to copy to clipboard:', err);
    });
  }
}