import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-art-generator',
  templateUrl: './art-generator.component.html',
  styleUrls: ['./art-generator.component.css']
})
export class ArtGeneratorComponent implements OnInit {

  artForm = this.formBuilder.group({
    keyword: ''
  });

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
  }

  handleSubmit(): void {
    console.log(this.artForm.value);
    this.http.post<GenerateResults>('http://localhost:3000/generator', {key: this.artForm.value.keyword}).subscribe(data => {
      console.log(data.okay);
    })

    const params = new HttpParams().append('key', 12345);
    this.http.get('http://localhost:3000/generator/id', {params: params}).subscribe(data => {
      console.log(data);
    })
  }

}

interface GenerateResults {
  okay: string;
}
