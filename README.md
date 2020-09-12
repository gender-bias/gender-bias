# Reading for Gender Bias

***Promote gender equality by identifying potential gender bias in letters of recommendation and evaluations***

***Autocorrect for bias***

Implicit gender bias in evaluations negatively impacts women at every stage of her career. The goal of this project is to create a web-based text analysis tool that scans and reveals language bias associated with evaluations and letters of recommendation written for trainees and applicants.  The tool will provide a summary of potential changes to the writer to help them remove bias.  The hope is that by bringing awareness to the existence of implicit bias, we can change how evaluations for women are drafted and judged, thereby providing a concrete way to tackle gender disparities.

## Welcome!

Thank you for visiting the Reading for Gender Bias project!

This document (the README file) introduces you to the project.  Feel free to explore by section or just scroll through.

* [What is the project about? (And why does it matter?)](#what-is-the-project-about)
* [Usage](#usage)
* [About the founder](#about-the-founder)
* [How can you get involved?](#how-can-you-get-involved)
* [Contact me](#contact-me)
* [Learn more](#learn-more)

## What is the project about?

### The problem

* Gender disparities exist in medicine, science, business, and many other professions
* Letters of recommendation and evaluations written for women differ in key ways from letters written for men
* The differences impact everything from how women are graded in a class to whether they are hired or promoted
* Most writers (men and women) are unaware of gender bias in their writing

So, even if someone wants to write a really strong letter for a woman, they will probably include language that reflects [implicit bias][link_implicitbias], which weakens the letter.

### The solution

Reading for Gender Bias is a web-based text analysis tool that:

* Scans evaluations or letters for language associated with bias
* Summarizes changes that would reduce bias for the writer
* Increases awareness of gender bias

## Usage

This document is currently a work-in-progress; please feel free to ask for clarification in the Issues tab of this repository, or on our slack workspace (details below).

### Installation

Currently, the most reliable way to download and start using this code is to clone it from this repository and install it using pip:

```shell
git clone https://github.com/gender-bias/gender-bias
cd gender-bias
pip3 install -e .
```

> **NOTE**: The last line in the above snippet installs this library in "editable" mode, which is probably fine while the library is in a state of flux.

This installation process will add a new command-line tool to your PATH, called `genderbias`.

To install the dependencies, run:
`pip3 install -r requirements.txt`

### Usage

#### Learning about usage

```shell
genderbias -h

usage: genderbias [-h] [--file FILE] [--json] [--list-detectors]
                  [--detectors DETECTORS]

CLI for gender-bias detection

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  The file to check
  --json, -j            Enable JSON output, instead of text
  --list-detectors      List the available detectors
  --detectors DETECTORS
                        Use specific detectors, not all available
```

You can probably ignore most of these options when getting started.

#### Checking a document

There are two ways to check a document: 

##### Option 1: Standard-In

This option streams a file from stdin and writes its suggestions to stdout. You can use it like this:

```shell
cat my-file.txt | genderbias
```

If you don't have a text file handy, you can try it out on one of ours:

```shell
cat ./example_letters/letterofRecW | genderbias
```

The tool will print its suggestions out to stdout:

```
Effort vs Accomplishment
 [516-527]: Effort vs Accomplishment: The word 'willingness' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 [2915-2926]: Effort vs Accomplishment: The word 'willingness' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 [3338-3347]: Effort vs Accomplishment: The word 'dedicated' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 [3492-3502]: Effort vs Accomplishment: The word 'commitment' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 [3524-3533]: Effort vs Accomplishment: The word 'tenacious' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 [3706-3716]: Effort vs Accomplishment: The word 'commitment' tends to speak about effort more than accomplishment. (Try replacing with phrasing that emphasizes accomplishment.)
 SUMMARY: This document has a high ratio (6:1) of words suggesting effort to words suggesting concrete accomplishment.
 ```
 
If you'd rather that the tool print its suggestions to another file, you can use the following:

```shell
cat ./example_letters/letterofRecW | genderbias > edits-to-made.txt
```

##### Option 2: Specify a file with a flag

This functionality is EXACTLY the same; just a matter of how you prefer to run the tool!

```shell
genderbias -f ./example_letters/letterofRecW
```

The `-f` or `--file` flag can be used to specify a file.

### How to interpret output

The output of this tool is a _character-index span_ that you can think of as "highlighting" the problematic (or potentially-problematic) text. Our intention is to add a more human-readable form as well; **if you're interested in helping develop that capability, please get in touch!**

### Using the tool as a REST server

The tool can also be run as a REST server in order to operate on text sent from a front-end — for example, [our client-side website](https://github.com/gender-bias/reading-for-genderbias-web). To run the server, run the following:

```shell
genderbias-server
```

This will start a Flask server listening on port 5000.

To use this server, send a POST requests to the `/check` endpoint, with a JSON body of the following form:

```json
{
    "text": "My text goes here"
}
```

For example, in Python, using `requests`:

```python
import requests

response = requests.post(
    "http://localhost:5000/check", 
    headers={"Content-Type": "application/json"}, 
    json={"text": "this is my text"}
)

print(response.json())
```

The response is JSON of the form:

```json
{
    "issues": List[genderbias.Issue],
    "text": <the same text you sent, for reference>
}
```



## About the founder

[Mollie][link_Mollie] is a medical student and a future neuroscientist who would like to make the world a better place.

The development of this project is mentored by [Jason][link_Jason] as part of [Mozilla Open Leaders][link_mozilla] and started in 2018.

## How can you get involved?

So glad you asked!  WooHoo!

Help in any way you can!

We need expertise in coding, web design, program development, documentation, and technical writing.  We're using Python for the text analysis. I've created issues around different rules/signals to search for in letters.  Example letters can be found [here](https://github.com/molliem/gender-bias/tree/master/example_letters).

If you think you can help in any of these areas or in an area I haven't thought of yet, please check out our [contributors' guidelines](CONTRIBUTING.md) and our [roadmap](https://github.com/molliem/gender-bias/issues/1).

The goal of this project is to promote gender equity, so we want to maintain a positive and supportive environment for everyone who wants to participate.  Please follow the [Mozilla Community Participation Guidelines](https://www.mozilla.org/en-US/about/governance/policies/participation/) in all interactions on and offline.  Thanks!

## Contact me

If you want to report a problem or suggest an improvement, please [open an issue](../../issues) at this github repository.  You can also reach [Mollie](link_Mollie) by email (mollie@biascorrect.com) or on [twitter](https://twitter.com/MollieMarr).

## Learn more

* [Contributors' guidelines](CONTRIBUTING.md)
* [Roadmap](https://github.com/molliem/gender-bias/issues/1)

Studies on gender bias show that letters/evaluations written for women are:

* Less likely to mention [publications, projects, and research](#publications-projects-and-research)
* Less likely to include [superlatives](#superlatives) ('She was the best, the top, the greatest')
* Less likely to use [nouns](#nouns) ('He was a researcher' while 'she taught')
* More likely to include [minimal assurance](#minimal-assurance) ('She can do the job') rather than a strong endorsement
* More likely to highlight [effort](#effort) ('She is hard-working') instead of highlighting accomplishments ('her research')
* More likely to discuss [personal life](#personal-life) and fail to use formal titles
* More likely to include [gender stereotypes](#gender-stereotypes) ('She is compassionate' while 'he is a leader') and emotion-focused words
* More likely to [raise doubt](#raise-doubt)
* [Shorter](#shorter)


## THANK YOU!!!

## References

### Publications, Projects, and Research
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]

### Superlatives
* Dutt, K., Pfaff, D. L., Bernstein, A. F., Dillard, J. S., & Block, C. J. (2016). Gender differences in recommendation letters for postdoctoral fellowships in geoscience. Nature Geoscience, 9(11), 805. [[Link](https://www.nature.com/articles/ngeo2819)]
* Schmader, T., Whitehead, J., & Wysocki, V. H. (2007). A linguistic comparison of letters of recommendation for male and female chemistry and biochemistry job applicants. Sex Roles, 57(7-8), 509-514. [[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2572075/)] [[PDF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2572075/pdf/nihms72978.pdf)]

### Nouns
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]

### Minimal Assurance
* Isaac, C., Chertoff, J., Lee, B., & Carnes, M. (2011). Do students’ and authors’ genders affect evaluations? A linguistic analysis of medical student performance evaluations. Academic Medicine, 86(1), 59. [[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/) [[PDF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/pdf/nihms363051.pdf)]
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]

### Effort
* Deaux, K. & Emswiller, T., "Explanations of successful performance on sex-linked tasks: What is skill for the male is luck for the female," Journal of Personality and Social Psychology 29(1974): 80-85 [[Link](http://psycnet.apa.org/record/1974-20859-001)]
* Isaac, C., Chertoff, J., Lee, B., & Carnes, M. (2011). Do students’ and authors’ genders affect evaluations? A linguistic analysis of medical student performance evaluations. Academic Medicine, 86(1), 59. [[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/) [[PDF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/pdf/nihms363051.pdf)]
* Steinpreis, R., Anders, K.A., & Ritzke, D., "The impact of gender on the review of the curricula vitae of job applicants and tenure candidates: A national empirical study," Sex Roles 41(1999): 509-528 [[Link](https://link.springer.com/article/10.1023/A:1018839203698)] [[PDF](https://pdfs.semanticscholar.org/bb0f/52062572e83c07b51d3f83ad937633a4637e.pdf)]

### Personal Life
* Isaac, C., Chertoff, J., Lee, B., & Carnes, M. (2011). Do students’ and authors’ genders affect evaluations? A linguistic analysis of medical student performance evaluations. Academic Medicine, 86(1), 59. [[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/) [[PDF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3321359/pdf/nihms363051.pdf)]
* Madera, J. M., Hebl, M. R., & Martin, R. C. (2009). Gender and letters of recommendation for academia: Agentic and communal differences. Journal of Applied Psychology, 94(6), 1591. [[Link](http://psycnet.apa.org/record/2009-21033-018)] [[PDF](https://eswnonline.org/wp-content/uploads/gravity_forms/23-b28d66b6400f67d9648a049f8faf44e0/2015/05/Madera2009_Gender-and-letters-of-recommendation.pdf)]
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]

### Gender Stereotypes
* Axelson RD, Solow CM, Ferguson KJ, Cohen MB.  Assessing implicit gender bias in Medical Student Performance Evaluations. Eval Health Prof. 2010 Sep;33(3):365-85. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0163278710375097?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%3dpubmed)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0163278710375097)]
* Eagly, A.H.; Karau, S.J., "Role congruity theory of prejudice toward female leaders," Psychological Review 109, no. 3 (July 2002): 573-597.; Ridgeway, 2002. [[Link](http://psycnet.apa.org/record/2002-13781-007)] [[PDF](https://www.rci.rutgers.edu/~search1/pdf/Eagley_Role_Conguity_Theory.pdf)]
* Foschi M. Double standards for competence: theory and research. Ann Rev Soc. 2000;26:21–42. [[Link](http://psycnet.apa.org/record/2000-02783-002)] [[PDF](http://search.committee.module.rutgers.edu/pdf/2787021.pdf)]
* Gaucher, D., Friesen, J., & Kay, A. C. (2011, March 7). Evidence That Gendered Wording in Job Advertisements Exists and Sustains Gender Inequality. Journal of Personality and Social Psychology. [[Link](http://psycnet.apa.org/record/2011-04642-001)] [[PDF](https://www.sussex.ac.uk/webteam/gateway/file.php?name=gendered-wording-in-job-adverts.pdf&site=7)]
* Hirshfield LE. ‘‘She’s not good with crying’’: the effect of gender expectations on graduate students’ assessments of their principal investigators. Gender Educ. 2014;26(6):601–617. [[Link](https://www.tandfonline.com/doi/abs/10.1080/09540253.2014.940036)]
* Madera, J. M., Hebl, M. R., & Martin, R. C. (2009). Gender and letters of recommendation for academia: Agentic and communal differences. Journal of Applied Psychology, 94(6), 1591. [[Link](http://psycnet.apa.org/record/2009-21033-018)] [[PDF](https://eswnonline.org/wp-content/uploads/gravity_forms/23-b28d66b6400f67d9648a049f8faf44e0/2015/05/Madera2009_Gender-and-letters-of-recommendation.pdf)]
* Ross DA, Boatright D, Nunez-Smith M, Jordan A, Chekroud A, Moore EZ (2017) Differences in words used to describe racial and gender groups in Medical Student Performance Evaluations. PLoS ONE 12(8): e0181659. [[Link](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0181659)] [[PDF](http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0181659&type=printable)]
* Sprague J, Massoni K. Student evaluations and gendered expectations: what we can’t count can hurt us. Sex Roles. 2005;53(11):779–793. [[Link](http://psycnet.apa.org/record/2008-14048-001)] [[PDF](https://www.researchgate.net/profile/Joey_Sprague/publication/227320290_Student_Evaluations_and_Gendered_Expectations_What_We_Can%27t_Count_Can_Hurt_Us/links/53dfa71e0cf27a7b83069ecb/Student-Evaluations-and-Gendered-Expectations-What-We-Cant-Count-Can-Hurt-Us.pdf?origin=publication_detail)]
* Steinpreis RE, Anders KA, Ritzke D. The impact of gender on the review of the curricula vitae of job applicants and tenure candidates: a national empirical study. Sex Roles. 1999;41(7):509–528. [[Link](https://link.springer.com/article/10.1023/A:1018839203698)] [[PDF](https://pdfs.semanticscholar.org/bb0f/52062572e83c07b51d3f83ad937633a4637e.pdf)]
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]
* Wenneras C, Wold A. Nepotism and sexism in peer review. Nature. 1997;387(6631):341–343. [[Link](https://www.nature.com/articles/387341a0)] [[PDF](https://www.cs.utexas.edu/users/mckinley/notes/ww-nature-1997.pdf)]

### Raise Doubt
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]
* Madera, J. M., Hebl, M. R., Dial, H., Martin, R., & Valian, V. (2019). Raising doubt in letters of recommendation for academia: gender differences and their impact. Journal of Business and Psychology, 34(3), 287-303.
[[Link](http://link.springer.com/10.1007/s10869-018-9541-1)]

### Shorter
* Dutt, K., Pfaff, D. L., Bernstein, A. F., Dillard, J. S., & Block, C. J. (2016). Gender differences in recommendation letters for postdoctoral fellowships in geoscience. Nature Geoscience, 9(11), 805. [[Link](https://www.nature.com/articles/ngeo2819)]
* Trix, F. & Psenka, C., "Exploring the color of glass: Letters of recommendation for female and male medical faculty," Discourse & Society 14(2003): 191-220. [[Link](http://journals.sagepub.com/doi/abs/10.1177/0957926503014002277)] [[PDF](http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277)]

[link_implicitbias]: https://en.wikipedia.org/wiki/Implicit_stereotype
[link_Jason]: https://twitter.com/jaclark
[link_Mollie]: https://twitter.com/MollieMarr
[link_mozilla]: https://mozilla.github.io/leadership-training/
