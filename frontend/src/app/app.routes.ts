import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AdvancedEditComponent } from './pages/advanced-edit/advanced-edit.component';
import { AboutComponent } from './pages/about/about.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'advanced-edit', component: AdvancedEditComponent },
    { path: 'about', component: AboutComponent }
];