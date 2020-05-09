import { TestBed } from '@angular/core/testing';

import { TextFileService } from './text-file.service';

describe('TextFileService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TextFileService = TestBed.get(TextFileService);
    expect(service).toBeTruthy();
  });
});
