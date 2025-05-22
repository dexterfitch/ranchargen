import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  error = '';
  loading = false;

  onRouteActivate(component: any): void {
    // Comment out below for testing Error and Loading messages
    if (component.errorChange) {
      component.errorChange.subscribe((err: string) => this.error = err);
    }
    if (component.loadingChange) {
      component.loadingChange.subscribe((isLoading: boolean) => this.loading = isLoading);
    }
  }
}