import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Character } from '../../models/character.model';
import { CharacterService } from '../../services/character.service';
import { FormsModule } from '@angular/forms';

type CharacterTraitKey = 'type' | 'occupation' | 'style' | 'disposition' | 'accessory' | 'palette';

@Component({
  standalone: true,
  selector: 'app-advanced-edit',
  templateUrl: './advanced-edit.component.html',
  styleUrls: ['./advanced-edit.component.scss'],
  imports: [CommonModule, FormsModule]
})
export class AdvancedEditComponent implements OnInit {
  character: Character | null = null;

  castKey(key: string): CharacterTraitKey {
    return key as CharacterTraitKey;
  }

  readonly traitKeys: CharacterTraitKey[] = [
    'type',
    'occupation',
    'style',
    'disposition',
    'accessory',
    'palette'
  ];

  locked: Record<CharacterTraitKey, boolean> = {
    type: false,
    occupation: false,
    style: false,
    disposition: false,
    accessory: false,
    palette: false
  };

  constructor(private characterService: CharacterService) {}

  ngOnInit(): void {
    this.getInitialCharacter();
  }

  getInitialCharacter(): void {
    this.characterService.getRandomCharacter().subscribe({
      next: (data) => {
        this.character = data;
      },
      error: (err) => {
        console.error('Error fetching character:', err);
      }
    });
  }

  randomizeUnlocked(): void {
    if (!this.character) return;

    this.characterService.getRandomCharacter().subscribe({
      next: (newData) => {
        this.traitKeys.forEach((key) => {
          if (!this.locked[key]) {
            if (key === 'palette') {
              this.character!.palette = newData.palette;
            } else {
              (this.character as any)[key] = (newData as any)[key];
            }
          }
        });
      },
      error: (err) => {
        console.error('Error randomizing character:', err);
      }
    });
  }
}