import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { PredictionComponent } from './prediction/prediction.component';
import { ContactComponent } from './contact/contact.component';
import { FooterComponent } from './footer/footer.component';
import { FaqComponent } from './faq/faq.component';
import { RegisterComponent } from './components/register/register.component';
import { LoginComponent } from './register/login/login.component';
import { PatientRegisterComponent } from './register/patient-register/patient-register.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    PredictionComponent,
    ContactComponent,
    FooterComponent,
    FaqComponent,
    RegisterComponent,
    LoginComponent,
    PatientRegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
