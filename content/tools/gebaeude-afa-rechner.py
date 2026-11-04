# -*- coding: utf-8 -*-
"""Gebäude-AfA-Rechner: lineare AfA für vermietete Gebäude im Privatvermögen (§ 7 Abs. 4 S. 1 Nr. 2 EStG),
im Anschaffungsjahr monatsgenau (§ 7 Abs. 1 S. 4 EStG), ohne Grund und Boden.
Rechenweg wie in der Excel-Vorlage Anlage V 2026 (Blatt AfA): Bemessungsgrundlage = (Kaufpreis + Nebenkosten) × (1 − Anteil Grund und Boden),
Satz nach Fertigstellungsjahr, Kaufjahr × (13 − Anschaffungsmonat) / 12. Zusätzlich Rechenhilfe 15-%-Grenze (§ 6 Abs. 1 Nr. 1a EStG)."""
META = {
    "slug": "gebaeude-afa-rechner",
    "name": "Gebäude-AfA-Rechner",
    "title": "Gebäude-AfA-Rechner: Abschreibung für vermietete Immobilien",
    "description": "AfA für ein vermietetes Haus oder eine Eigentumswohnung berechnen: Kaufpreis ohne Grund und Boden, 2 %, 2,5 % oder 3 % je nach Baujahr, im Kaufjahr monatsgenau. Kostenlos.",
    "card_text": "Kaufpreis und Nebenkosten ohne Grund und Boden, Satz nach Fertigstellungsjahr, AfA im Kaufjahr monatsgenau – mit 15-%-Grenze.",
    "llms": "Rechner für die lineare Gebäude-AfA im Privatvermögen: Bemessungsgrundlage aus Kaufpreis plus Kaufnebenkosten ohne Anteil Grund und Boden, Satz 3 % (fertiggestellt ab 2023), 2 % (1925–2022), 2,5 % (vor 1925) nach § 7 Abs. 4 S. 1 Nr. 2 EStG, im Kaufjahr monatsgenau (§ 7 Abs. 1 S. 4 EStG), optional selbst genutzter Flächenanteil, Rechenhilfe 15-%-Grenze für anschaffungsnahe Herstellungskosten (§ 6 Abs. 1 Nr. 1a EStG).",
    "date": "2026-11-04",
    "seo_title": "AfA-Rechner Immobilie: Gebäude-AfA 2 %, 2,5 %, 3 % berechnen",
    "eyebrow": "Kostenloser Rechner · § 7 EStG",
    "answer": "Vermieter schreiben das **Gebäude** ab, nicht den Grund und Boden: jährlich **2 %** (fertiggestellt 1925 bis 2022), **2,5 %** (vor 1925) oder **3 %** (ab 2023) von Kaufpreis plus Nebenkosten ohne Bodenanteil. Im Kaufjahr zählt die AfA **ab dem Monat der Anschaffung** (§ 7 EStG).",
    "order": 5,
    "faq": [
        ("Woher weiß ich den Anteil für Grund und Boden?", "Steht im Kaufvertrag eine Aufteilung, ist sie grundsätzlich maßgeblich, solange sie die realen Wertverhältnisse nicht grundsätzlich verfehlt und wirtschaftlich haltbar ist (BFH, Urteil vom 21.07.2020, IX R 26/19). Fehlt sie, wird nach den Verkehrswerten von Boden und Gebäude aufgeteilt. Eine erste Orientierung gibt der Bodenrichtwert × Grundstücksfläche (bei Eigentumswohnungen Ihr Miteigentumsanteil). Das Finanzamt nutzt oft die Arbeitshilfe des Bundesfinanzministeriums zur Kaufpreisaufteilung – sie ist laut BFH aber nicht bindend."),
        ("Zählt das Baujahr oder das Kaufjahr?", "Für den Satz zählt das Jahr, in dem das Gebäude fertiggestellt wurde – meist das Baujahr. Ein 1968 gebautes Haus, das Sie 2024 kaufen, schreiben Sie mit 2 % ab. Das Kaufjahr bestimmt nur, ab wann die AfA läuft."),
        ("Kann ich schneller abschreiben?", "Ist die tatsächliche Nutzungsdauer kürzer als 50 Jahre (bei 2 %), 40 Jahre (2,5 %) bzw. 33 Jahre (3 %), dürfen Sie nach der kürzeren Dauer abschreiben – das müssen Sie nachweisen, etwa mit einem Gutachten (§ 7 Abs. 4 S. 2 EStG). Für neu gebaute Wohngebäude kommen unter engen Voraussetzungen die degressive AfA (§ 7 Abs. 5a EStG) oder die Sonderabschreibung nach § 7b EStG in Betracht. Beides rechnet dieser Rechner nicht."),
        ("Was ist mit Renovierungskosten nach dem Kauf?", "Instandsetzung und Modernisierung in den ersten drei Jahren nach dem Kauf sind Herstellungskosten, wenn sie ohne Umsatzsteuer 15 % der Anschaffungskosten des Gebäudes übersteigen (§ 6 Abs. 1 Nr. 1a EStG). Dann erhöhen sie die AfA-Bemessungsgrundlage, statt sofort abziehbar zu sein. Der Rechner zeigt die Grenze als Rechenhilfe; mehr dazu im Ratgeber zur Anlage V."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 7 EStG – Absetzung für Abnutzung (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__7.html"),
        ("§ 6 EStG – Bewertung, Abs. 1 Nr. 1a anschaffungsnahe Herstellungskosten (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__6.html"),
        ("§ 9 EStG – Werbungskosten, Abs. 1 S. 3 Nr. 7 AfA (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__9.html"),
        ("BMF-Schreiben vom 26.01.2026, IV C 1 - S 2253/00082/001/064 – Instandsetzung und Modernisierung von Gebäuden (PDF, via ivd.net)", "https://ivd.net/wp-content/uploads/2026/02/2026-01-26-instandsetzung-modernisierung-gebaeude-1.pdf"),
        ("BFH, Urteil vom 21.07.2020, IX R 26/19 – Kaufpreisaufteilung auf Grund und Gebäude (dejure.org)", "https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BFH&Datum=21.07.2020&Aktenzeichen=IX+R+26%2F19"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="kp">Kaufpreis (€)</label><input type="text" id="kp" inputmode="decimal" value="400.000" autocomplete="off"></div>
<div><label for="nk">Kaufnebenkosten (€)</label><input type="text" id="nk" inputmode="decimal" value="36.100" autocomplete="off"></div>
</div>
<p class="hint">Nebenkosten: Grunderwerbsteuer, Notar und Grundbuch für den Eigentumsübergang, Makler. Nicht dazu: Kosten für die Grundschuld (sofort abziehbar).</p>
<div class="row2">
<div><label for="gb">Anteil Grund und Boden (%)</label><input type="text" id="gb" inputmode="decimal" value="25" autocomplete="off"></div>
<div><label for="bj">Fertigstellungsjahr (Baujahr)</label><input type="text" id="bj" inputmode="numeric" value="1968" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="dat">Übergang von Besitz, Nutzen und Lasten</label><input type="date" id="dat" value="2024-07-01" min="1950-01-01" max="2100-12-31"></div>
<div><label for="eig">Selbst genutzter Anteil der Wohnfläche (%, optional)</label><input type="text" id="eig" inputmode="decimal" value="" placeholder="0" autocomplete="off"></div>
</div>
<p class="hint">Maßgeblich für den Beginn der AfA ist der Übergang laut Kaufvertrag, nicht der Notartermin. Den selbst genutzten oder unentgeltlich überlassenen Anteil tragen Sie nur ein, wenn Sie einen Teil des Hauses nicht vermieten.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Bemessungsgrundlage:</strong> Kaufpreis plus Kaufnebenkosten, abzüglich des Anteils für Grund und Boden. Grund und Boden nutzt sich nicht ab und wird nicht abgeschrieben.</p>
<p><strong>AfA-Satz</strong> nach dem Fertigstellungsjahr (§ 7 Abs. 4 S. 1 Nr. 2 EStG): fertiggestellt nach dem 31.12.2022 jährlich 3 %, vom 01.01.1925 bis 31.12.2022 jährlich 2 %, vor dem 01.01.1925 jährlich 2,5 %.</p>
<p><strong>Kaufjahr:</strong> Die Jahres-AfA vermindert sich um ein Zwölftel für jeden vollen Monat vor dem Monat der Anschaffung (§ 7 Abs. 1 S. 4 EStG). Bei Übergang im Juli zählen also 6/12, im Dezember 1/12. Danach gilt jedes Jahr die volle AfA, bis das Gebäude vollständig abgeschrieben ist.</p>
<p><strong>Eigennutzung:</strong> Wohnen Sie selbst im Haus, rechnet der Rechner den vermieteten Anteil vereinfacht nach Wohnfläche. Nur die AfA auf diesen Anteil ist Werbungskosten.</p>
<p><strong>Nicht abgebildet:</strong> nachträgliche Herstellungskosten, kürzere Nutzungsdauer per Gutachten, degressive AfA (§ 7 Abs. 5a EStG), Sonderabschreibung (§ 7b EStG), Gebäude im Betriebsvermögen, Erbschaft und Schenkung (dort führen Sie die AfA des Vorgängers fort).</p>
<p>Mehr dazu im Ratgeber <a href="anlage-v-vermietung.html#afa">Anlage V ausfüllen: Mieteinnahmen und Werbungskosten</a>. Die <a href="anlage-v.html">Excel-Vorlage Anlage V 2026</a> rechnet die AfA genauso und übernimmt sie in die Summen für die Steuererklärung.</p>
<p class="note">Allgemeine Information, keine Steuerberatung. Im Einzelfall hilft eine Steuerberatung.</p>"""

SCRIPT = r"""
function r2(x){return Math.round((x+(x>=0?1e-9:-1e-9))*100)/100}
var MON=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'];
function calc(){var r=$('res'),kp=num($('kp').value),nk=num($('nk').value),gb=num($('gb').value),bjs=($('bj').value||'').trim(),bj=/^\d{4}$/.test(bjs)?+bjs:null,dv=$('dat').value,eig=num($('eig').value),out='';
 if(kp===null||kp<=0){r.innerHTML=light('y','Bitte den Kaufpreis eingeben.');return}
 if(nk===null)nk=0;
 if(nk<0){r.innerHTML=light('y','Die Nebenkosten dürfen nicht negativ sein.');return}
 if(gb===null||gb<0||gb>=100){r.innerHTML=light('y','Bitte den Anteil für Grund und Boden in Prozent eingeben (0 bis unter 100), z. B. 25.');return}
 if(bj===null||bj<1500||bj>2100){r.innerHTML=light('y','Bitte das Fertigstellungsjahr vierstellig eingeben, z. B. 1968.');return}
 var p=dv.split('-');if(p.length!==3||+p[0]<1950||+p[0]>2100){r.innerHTML=light('y','Bitte das Datum des Übergangs eingeben (zwischen 1950 und 2100).');return}
 var ky=+p[0],km=+p[1];
 if(eig===null)eig=0;
 if(eig<0||eig>100){r.innerHTML=light('y','Der selbst genutzte Anteil muss zwischen 0 und 100 % liegen.');return}
 if(bj>ky){r.innerHTML=light('y','Das Fertigstellungsjahr liegt nach dem Kaufjahr – bitte prüfen.','Beim Kauf vom Bauträger vor Fertigstellung oder beim eigenen Neubau beginnt die AfA erst mit der Fertigstellung. Diesen Fall rechnet der Rechner nicht.');return}
 var satz=bj>=2023?3:(bj>=1925?2:2.5),txt=bj>=2023?'fertiggestellt nach dem 31.12.2022':(bj>=1925?'fertiggestellt 1925 bis 2022':'fertiggestellt vor 1925');
 var ak=r2(kp+nk),geb=r2(ak*(100-gb)/100),voll=r2(geb*satz/100),mon=13-km,erst=r2(voll*mon/12);
 var rest=r2(geb-erst),n=Math.ceil(rest/voll-1e-9),endj=ky+n,last=r2(rest-(n-1)*voll);
 var ant=(100-eig)/100;
 if(eig>=100){out+=light('r','Bei 100 % Eigennutzung gibt es keine AfA als Werbungskosten.','Die AfA ist nur für vermietete Gebäude(teile) abziehbar. Die Werte unten zeigen die rechnerische AfA für das ganze Gebäude.')}
 out+=light('g','AfA-Satz '+fmt(satz,satz%1?1:0)+' % ('+txt+'): '+eur(voll)+' im vollen Jahr.','Im Kaufjahr '+ky+' ab '+MON[km-1]+': '+mon+'/12 = '+eur(erst)+'.');
 out+='<div class="kpis"><div class="kpi"><span>AfA-Bemessungsgrundlage</span><b>'+eur(geb)+'</b></div><div class="kpi"><span>AfA-Satz</span><b>'+fmt(satz,satz%1?1:0)+' %</b></div></div>';
 out+='<div class="kpis"><div class="kpi"><span>AfA '+ky+' ('+mon+'/12)</span><b>'+eur(erst)+'</b></div><div class="kpi"><span>AfA ab '+(ky+1)+' pro Jahr</span><b>'+eur(voll)+'</b></div></div>';
 var rows='<tr><td>Kaufpreis + Nebenkosten</td><td style="white-space:nowrap">'+eur(ak)+'</td></tr>'
  +'<tr><td>− Grund und Boden ('+fmt(gb,gb%1?2:0)+' %)</td><td style="white-space:nowrap">'+eur(r2(ak-geb))+'</td></tr>'
  +'<tr><td><strong>= Gebäude (Bemessungsgrundlage)</strong></td><td style="white-space:nowrap"><strong>'+eur(geb)+'</strong></td></tr>'
  +'<tr><td>AfA '+ky+' ('+(km===12?'Dezember':MON[km-1]+' bis Dezember')+')</td><td style="white-space:nowrap">'+eur(erst)+'</td></tr>'
  +'<tr><td>AfA '+(ky+1)+' bis '+(endj-1)+' je Jahr</td><td style="white-space:nowrap">'+eur(voll)+'</td></tr>'
  +'<tr><td>Rest '+endj+' (voll abgeschrieben)</td><td style="white-space:nowrap">'+eur(last)+'</td></tr>';
 if(eig>0&&eig<100)rows+='<tr><td>Davon vermietet ('+fmt(100-eig,(100-eig)%1?2:0)+' % der Wohnfläche): AfA '+ky+'</td><td style="white-space:nowrap">'+eur(r2(erst*ant))+'</td></tr>'
  +'<tr><td>Davon vermietet: AfA ab '+(ky+1)+' je Jahr</td><td style="white-space:nowrap">'+eur(r2(voll*ant))+'</td></tr>';
 out+='<div class="tblwrap"><table class="tbl"><tr><th>Rechenweg</th><th>Betrag</th></tr>'+rows+'</table></div>';
 if(eig>0&&eig<100)out+='<p class="hint">Im Formular (so in der Anlage V 2025) steht die Gebäude-AfA dann in der Spalte „verhältnismäßige Zuordnung“: Gesamtbetrag (im Kaufjahr '+eur(erst)+', danach '+eur(voll)+') und abzugsfähiger Anteil '+fmt(100-eig,(100-eig)%1?2:0)+' %.</p>';
 if(bj>=2023)out+='<p class="hint">Für neu gebaute Wohngebäude kommen unter engen Voraussetzungen auch die degressive AfA (§ 7 Abs. 5a EStG) oder die Sonderabschreibung nach § 7b EStG in Betracht. Diese rechnet der Rechner nicht – lassen Sie sich beraten.</p>';
 if(eig>=100){r.innerHTML=out;return}
 var g15=r2(geb*0.15),gv=r2(geb*ant*0.15),bez=eig>0&&eig<100?gv:g15;
 out+='<h3 style="margin-top:22px">Rechenhilfe: 15-%-Grenze nach dem Kauf</h3>';
 out+='<p class="hint">Instandsetzung und Modernisierung, die innerhalb von drei Jahren nach dem Übergang am '+('0'+p[2]).slice(-2)+'.'+('0'+p[1]).slice(-2)+'.'+p[0]+' durchgeführt werden, sind Herstellungskosten, wenn sie <strong>ohne Umsatzsteuer</strong> 15 % der Anschaffungskosten des Gebäudes übersteigen (§ 6 Abs. 1 Nr. 1a EStG). Grenze hier: 15 % von '+eur(geb)+' = <strong>'+eur(g15)+' netto</strong>'
  +(eig>0&&eig<100?'. Bei teilweiser Eigennutzung prüft die Finanzverwaltung je Gebäudeteil – vereinfacht nach Wohnfläche entfallen auf den vermieteten Teil '+eur(r2(geb*ant))+' Anschaffungskosten, die Grenze dafür läge bei <strong>'+eur(gv)+' netto</strong> (nur für Kosten, die auf den vermieteten Teil entfallen)':'')
  +'. Bei Rechnungen mit durchgehend 19 % Umsatzsteuer entspricht das '+eur(r2(bez*1.19))+' brutto.</p>';
 out+='<p class="hint">Schönheitsreparaturen zählen mit, jährlich übliche Arbeiten wie Wartung nicht. Wird die Grenze überschritten, sind alle diese Kosten nicht sofort abziehbar, sondern erhöhen die AfA – auch rückwirkend für Vorjahre. Nur eine Rechenhilfe: Ob eine Maßnahme dazugehört, wie bei mehreren Gebäudeteilen aufzuteilen ist und wann die Frist genau endet, klären Sie im Zweifel mit Ihrer Steuerberatung.</p>';
 r.innerHTML=out}
['kp','nk','gb','bj','dat','eig'].forEach(function(i){$(i).addEventListener('input',calc);$(i).addEventListener('change',calc)});calc();
"""
