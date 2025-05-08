import { Component, Input, Renderer2, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Character } from '../../models/character.model';

@Component({
  selector: 'app-character-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './character-card.component.html',
  styleUrls: ['./character-card.component.scss']
})
export class CharacterCardComponent {
  @Input() character: Character | null = null;
  @Input() title: string | null = null;

  @ViewChild('liveRegion', { static: true }) liveRegion!: ElementRef;
  liveMessage = '';
  
  constructor(private renderer: Renderer2) {}
  
  copyToClipboard(color: string, event: Event): void {
    const swatch = event.currentTarget as HTMLElement;
    if (!swatch) return;

    navigator.clipboard.writeText(color).then(() => {
        const tooltip = this.renderer.createElement('span');
        this.renderer.addClass(tooltip, 'tooltip');
        const text = this.renderer.createText('Copied!');
        this.renderer.appendChild(tooltip, text);
        this.renderer.appendChild(swatch, tooltip);
        this.liveMessage = 'Copied to clipboard!';

        setTimeout(() => {
            this.renderer.removeChild(swatch, tooltip);
            this.liveMessage = '';
        }, 1000);
    }).catch(err => {
        console.error('Failed to copy to clipboard:', err);
    });
  }
}