# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import chembl_core_db.db.customFields


class Migration(migrations.Migration):

    dependencies = [
        ('chembl_core_model', '0002_auto_20150323_0929'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='celldictionary',
        #     name='downgraded',
        #     field=chembl_core_db.db.customFields.ChemblNullableBooleanField(default=False, help_text='Indicates the cell line has been removed (if set to 1)'),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='chemblidlookup',
        #     name='entity_type',
        #     field=chembl_core_db.db.customFields.ChemblCharField(help_text='Type of entity (e.g., COMPOUND, ASSAY, TARGET)', max_length=50, choices=[(b'ASSAY', b'ASSAY'), (b'CELL', b'CELL'), (b'COMPOUND', b'COMPOUND'), (b'DOCUMENT', b'DOCUMENT'), (b'TARGET', b'TARGET')]),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='compoundproperties',
        #     name='acd_most_bpka',
        #     field=chembl_core_db.db.customFields.ChemblPositiveDecimalField(help_text='The most basic pKa calculated using ACDlabs v12.01', null=True, max_digits=9, decimal_places=2, blank=True),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='defineddailydose',
        #     name='ddd_value',
        #     field=chembl_core_db.db.customFields.ChemblPositiveDecimalField(help_text='Value of defined daily dose', null=True, max_digits=9, decimal_places=2, blank=True),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='drugmechanism',
        #     name='selectivity_comment',
        #     field=chembl_core_db.db.customFields.ChemblCharField(blank=True, max_length=100, null=True, help_text='Additional comments regarding the selectivity of the drug', choices=[(b'Broad spectrum', b'Broad spectrum'), (b'EDG5 less relevant', b'EDG5 less relevant'), (b'FGFR 1, 2 + 3', b'FGFR 1, 2 + 3'), (b'M3 selective', b'M3 selective'), (b"Non-selective but type 5 receptor is overexpressed in Cushing's disease", b"Non-selective but type 5 receptor is overexpressed in Cushing's disease"), (b'Selective', b'Selective'), (b'Selective for the brain omega-1 receptor (i.e. BZ1-type, i.e. alpha1/beta1/gamma2-GABA receptor)', b'Selective for the brain omega-1 receptor (i.e. BZ1-type, i.e. alpha1/beta1/gamma2-GABA receptor)'), (b'Selectivity for types 2, 3 and 5', b'Selectivity for types 2, 3 and 5'), (b'selectivity for beta-3 containing complexes', b'selectivity for beta-3 containing complexes')]),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='proteinclassification',
        #     name='downgraded',
        #     field=chembl_core_db.db.customFields.ChemblBooleanField(default=False),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='targetcomponents',
        #     name='homologue',
        #     field=chembl_core_db.db.customFields.ChemblPositiveIntegerField(default=0, help_text='Indicates that the given component is a homologue of the correct component (e.g., from a different species) when set to 1. This may be the case if the sequence for the correct protein/nucleic acid cannot be found in sequence databases. A value of 2 indicates that the sequence given is a representative of a species group, e.g., an E. coli protein to represent the target of a broad-spectrum antibiotic.', choices=[(0, b'0'), (1, b'1'), (2, b'2')]),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='targetcomponents',
        #     name='relationship',
        #     field=chembl_core_db.db.customFields.ChemblCharField(default='UNCURATED', max_length=20, choices=[(b'COMPARATIVE PROTEIN', b'COMPARATIVE PROTEIN'), (b'EQUIVALENT PROTEIN', b'EQUIVALENT PROTEIN'), (b'FUSION PROTEIN', b'FUSION PROTEIN'), (b'GROUP MEMBER', b'GROUP MEMBER'), (b'INTERACTING PROTEIN', b'INTERACTING PROTEIN'), (b'PROTEIN SUBUNIT', b'PROTEIN SUBUNIT'), (b'RNA', b'RNA'), (b'RNA SUBUNIT', b'RNA SUBUNIT'), (b'SINGLE PROTEIN', b'SINGLE PROTEIN'), (b'UNCURATED', b'UNCURATED'), (b'SUBUNIT', b'SUBUNIT')]),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='targetdictionary',
        #     name='downgraded',
        #     field=chembl_core_db.db.customFields.ChemblBooleanField(default=False, help_text='Flag to indicate that the target is downgraded (if equal to 1)'),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='targetdictionary',
        #     name='species_group_flag',
        #     field=chembl_core_db.db.customFields.ChemblBooleanField(default=False, help_text="Flag to indicate whether the target represents a group of species, rather than an individual species (e.g., 'Bacterial DHFR'). Where set to 1, indicates that any associated target components will be a representative, rather than a comprehensive set."),
        #     preserve_default=True,
        # ),
        # migrations.AlterModelTable(
        #     name='actiontype',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='activities',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='activitystdslookup',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='assayparameters',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='assays',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='assaytype',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='atcclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='bindingsites',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='biocomponentsequences',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='biotherapeuticcomponents',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='biotherapeutics',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='celldictionary',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='chemblidlookup',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='componentclass',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='componentdomains',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='componentsequences',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='componentsynonyms',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='compoundimages',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='compoundproperties',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='compoundrecords',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='compoundstructuralalerts',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='compoundstructures',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='confidencescorelookup',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='curationlookup',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='datavaliditylookup',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='defineddailydose',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='docs',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='domains',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='drugmechanism',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='formulations',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='fracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='hracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='iracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='journalarticles',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='journals',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='ligandeff',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='mechanismrefs',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculeatcclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculedictionary',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculefracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculehierarchy',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculehracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculeiracclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='moleculesynonyms',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='organismclass',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='parametertype',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='patentusecodes',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='predictedbindingdomains',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='productpatents',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='products',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='proteinclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='proteinclasssynonyms',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='proteinfamilyclassification',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='recorddrugproperties',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='relationshiptype',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='researchcompanies',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='researchstem',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='sitecomponents',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='source',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='structuralalerts',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='structuralalertsets',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='targetcomponents',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='targetdictionary',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='targetrelations',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='targettype',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='usanstems',
        #     table=None,
        # ),
        # migrations.AlterModelTable(
        #     name='version',
        #     table=None,
        # ),
    ]
