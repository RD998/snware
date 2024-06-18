from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField

class PastebinEntry(FlaskForm):
    bustype = SelectField(u'Type  Of Sale', choices=[('B2C', 'B2C'), ('B2B - Managers +', 'B2B Managers'), ('B2B - Directors +', 'B2B Directors')])
    irp = SelectField(u'IR Percentage', choices=[('IR  76-100%', '76-100%'), ('IR  50-75%', '50-75%'), ('IR 25-49%', '25-49%'), ('IR < 25%', '< 25%')])
    time = SelectField(u'Timing', choices=[('<=10 min', '<=10 min'), ('11-15    min', '11-15    min'), ('16-20   min', '16-20   min'), ('21-25    min', '21-25    min'), ('26-30    min', '26-30    min')])
    countrys = SelectField(u'Select The Country', choices=[('United States', 'United States'), ('Canada', 'Canada'), ('Argentina', 'Argentina'), ('Australia & New Zealand', 'Australia & New Zealand'), ('Brazil', 'Brazil'), ('China', 'China'), ('France', 'France'), ('Germany', 'Germany'), ('Hong Kong', 'Hong Kong'), ('India', 'India'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Malaysia', 'Malaysia'), ('Mexico', 'Mexico'), ('Russia', 'Russia'), ('Singapore', 'Singapore'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('United Kingdom', 'United Kingdom')])
    submit = SubmitField('Submit')

class QuotationEntry(FlaskForm):
    lvlselect = SelectField(u'Complexity (4 -> high, 1 -> low)', choices=[('Level 1', 'Level 1'), ('Level 2', 'Level 2'), ('Level 3', 'Level 3'), ('Level 4', 'Level 4')])
    loiselect = SelectField(u'Select Length Of Interview', choices=[('5', '5 mins'), ('10', '10 mins'), ('15', '15 mins'), ('20', '20 mins'), ('25', '25 mins'), ('30', '30 mins'), ('35', '35 mins'), ('40', '40 mins'), ('45', '45 mins')])
    ContNo = IntegerField(u'Total Number Of Countries')
    BanNo = IntegerField(u'Total Number Of Banners')
    WeightNo = IntegerField(u'Total Number Of Weightings')
    submit = SubmitField('Submit')


class PastebinEntry2(FlaskForm):
    bustype = SelectField(u'Type  Of Sale', choices=[('B2C', 'B2C'), ('B2B - Manager and equivalent', 'B2B Managers'), ('B2B - Directors and above', 'B2B Directors')])
    irp = SelectField(u'IR Percentage', choices=[('IR  76-100%', '76-100%'), ('IR  50-75%', '50-75%'), ('IR 25-49%', '25-49%'), ('IR < 25%', '< 25%')])
    time = SelectField(u'Timing', choices=[('<=10 min', '<=10 min'), ('11-15    min', '11-15    min'), ('16-20   min', '16-20   min')])
    countrys = SelectField(u'Select The Country', choices=[('United States', 'United States'), ('Canada', 'Canada'), ('Argentina', 'Argentina'), ('Australia & New Zealand', 'Australia & New Zealand'), ('Brazil', 'Brazil'), ('China', 'China'), ('France', 'France'), ('Germany', 'Germany'), ('Hong Kong', 'Hong Kong'), ('India', 'India'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Malaysia', 'Malaysia'), ('Mexico', 'Mexico'), ('Russia', 'Russia'), ('Singapore', 'Singapore'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('United Kingdom', 'United Kingdom')])
    submit = SubmitField('Submit')
