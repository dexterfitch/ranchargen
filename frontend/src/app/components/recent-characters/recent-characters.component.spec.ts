import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentCharactersComponent } from './recent-characters.component';

describe('RecentCharactersComponent', () => {
  let component: RecentCharactersComponent;
  let fixture: ComponentFixture<RecentCharactersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecentCharactersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecentCharactersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
