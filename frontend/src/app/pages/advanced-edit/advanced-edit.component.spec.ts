import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdvancedEditComponent } from './advanced-edit.component';

describe('AdvancedEditComponent', () => {
  let component: AdvancedEditComponent;
  let fixture: ComponentFixture<AdvancedEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdvancedEditComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdvancedEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
