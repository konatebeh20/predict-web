import { Component } from '@angular/core';

@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html',
  styleUrls: ['./faq.component.scss']
})
export class FaqComponent {
  faqs = [
    {
      question: 'Comment fonctionne notre modèle de prédiction ?',
      answer: 'Notre modèle intègre des données multi-omiques pour analyser divers biomarqueurs et fournir des prédictions précises sur les résultats du traitement.',
      open: false
    },
    {
      question: 'Comment importer des données ?',
      answer: 'Vous pouvez importer des données directement via notre interface utilisateur après vous être connecté à votre compte clinique.',
      open: false
    },
    {
      question: 'Comment interpréter les résultats ?',
      answer: 'Les résultats fournis par notre modèle incluent des informations détaillées sur les biomarqueurs et les prédictions de réponse au traitement.',
      open: false
    }
  ];

  toggleFaq(faq: any) {
    faq.open = !faq.open;
  }
}
