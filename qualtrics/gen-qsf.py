# encoding: utf-8

import simplejson as json
import sys

def qsf(questions):
    null = None
    true = True
    false = False
    BL0 = []
    survey = {
            "SurveyElements": [
                {
                    "Element": "BL",
                    "Payload": [
                        {
                            "BlockElements": BL0,
                            "Description": "default",
                            "ID": "BL_6szFBnxpozQxln7",
                            "Type": "Default",
                            },
                        {
                            "BlockElements": [ ],
                            "Description": "Trash / Unused Questions",
                            "ID": "BL_3KqmYA4oBupoX8p",
                            "Type": "Trash"
                            }
                        ],
                    "PrimaryAttribute": "Survey Blocks",
                    "SecondaryAttribute": null,
                    "SurveyID": "SV_6G3iaYPb3lqPJEV",
                    "TertiaryAttribute": null
                    },
                {
                    "Element": "FL",
                    "Payload": {
                        "Flow": [
                            {
                                "FlowID": "FL_2",
                                "ID": "BL_6szFBnxpozQxln7",
                                "Type": "Block"
                                }
                            ],
                        "FlowID": "FL_1",
                        "Properties": {
                            "Count": 2
                            },
                        "Type": "Root"
                        },
                    "PrimaryAttribute": "Survey Flow",
                    "SecondaryAttribute": null,
                    "SurveyID": "SV_6G3iaYPb3lqPJEV",
                    "TertiaryAttribute": null
                    },
                {
                    "Element": "SO",
                    "Payload": {
                        "AnonymizeResponse": "No",
                        "AvailableLanguages": {
                            "HU": []
                            },
                        "BackButton": "true",
                        "BallotBoxStuffingPrevention": "false",
                        "CollectGeoLocation": "false",
                        "CustomStyles": {
                            "altRowStyles": {
                                "selector": ".Skin .ReadableAlt, .Skin .LightBG",
                                "styles": {
                                    "backgroundColor": null
                                    }
                                },
                            "borderStyles": {
                                "selector": ".Skin .CS .horizontalbar table.sliderGrid tr.xlabel th, .Skin .CS .horizontalbar .ylabel, .Skin .CS .horizontalbar table.sliderGrid tr td.value, .Skin .Slider .horizontalbar table.sliderGrid tr.xlabel th, .Skin .BorderColor, .Skin .DarkBorderColor, .Skin .Slider .horizontalbar table.sliderGrid tr td.value, .Skin thead, .Skin .GAP .ChoiceStructure thead th  ",
                                "styles": {
                                    "borderColor": null
                                    }
                                },
                            "choiceStyles": {
                                "selector": ".Skin .horizontalbar th.ylabel, .Skin .Matrix table td, .Skin .Matrix table th, .Skin .Matrix table thead th, .Skin .Matrix table thead td, .Skin .PGR .DragAndDrop .Items label, .Skin .QuestionBody ul.ChoiceStructure, .Skin .PGR .DragAndDrop .Group ul, .Skin .PGR .DragAndDrop .Group h2, .Skin .PGR .DragAndDrop .Items ul, .Skin .PGR .DragAndDrop .Items h2, .Skin .DD .QuestionBody table.ChoiceStructure, .Skin .PGR .DragAndDrop .NoColumns td.groupsContainerTd div ul, .Skin .PGR .DragAndDrop .NoColumns td.groupsContainerTd div h2, .Skin .SBS thead th, .Skin .SBS td, .Skin .SBS .Answers td, .Skin .SBS .Answers th, .SBS table.ChoiceStructure, .Skin .horizontalbar thead table.LabelDescriptions tr td, .Skin .horizontalbar thead tr td.NotApplicable, .QuestionBody th, .Skin .QuestionBody .MC .MAVR label, .Skin .QuestionBody .MC .SAVR label, .Skin .SBS thead th, .Skin .SBS td, .Skin .RO .DND ul li, .Skin .reg, .SkinInner .ChoiceStructure, .Skin thead, .Skin .GAP .ChoiceStructure thead th, .Skin .GAP .ChoiceStructure .c4, .Skin .GAP .ChoiceStructure th, .Skin .GAP .ChoiceStructure .WhyText, .SkinInner .ChoiceStructure .LightBG, .Skin .QuestionOuter.Highlight .Inner .reg, .Skin .QuestionOuter.Highlight .Inner .alt, .Skin .QuestionOuter.Highlight .Inner .ReadableAlt       ",
                                "styles": {
                                    "color": null,
                                    "fontFamily": "",
                                    "fontSize": "",
                                    "fontStyle": "",
                                    "fontWeight": "",
                                    "textDecoration": ""
                                    }
                                },
                            "customCSS": null,
                            "errorStyles": {
                                "selector": ".Skin .ValidationError",
                                "styles": {
                                    "backgroundColor": null,
                                    "borderColor": null,
                                    "color": null
                                    }
                                },
                            "errorStylesBG": {
                                "selector": ".Skin .HeaderValidationError, .Skin .HeaderValidationError li a",
                                "styles": {
                                    "backgroundColor": null,
                                    "color": null
                                    }
                                },
                            "footerStyles": {
                                "selector": ".Skin #Footer",
                                "styles": {
                                    "color": null
                                    }
                                },
                            "headerStyles": {
                                "selector": ".Skin div#Header",
                                "styles": {
                                    "color": null
                                    }
                                },
                            "highlightStyles": {
                                    "selector": ".Skin .QuestionOuter.Highlight .Inner, .Skin .QuestionOuter.Highlight .Inner .reg, .Skin .QuestionOuter.Highlight .Inner .alt, .Skin .QuestionOuter.Highlight .Inner .ReadableAlt",
                                    "styles": {
                                        "backgroundColor": null
                                        }
                                    },
                            "highlightStylesAlt": {
                                    "selector": ".Skin .QuestionOuter.Highlight .Inner .ReadableAlt, .Skin .QuestionOuter.Highlight .Inner .LightBG",
                                    "styles": {
                                        "backgroundColor": null
                                        }
                                    },
                            "pageStyles": {
                                    "selector": "#SurveyEngineBody",
                                    "styles": {
                                        "backgroundColor": null
                                        }
                                    },
                            "questionSeparatorStyles": {
                                    "selector": ".Skin .Separator",
                                    "styles": {
                                        "backgroundColor": null,
                                        "display": null
                                        }
                                    },
                            "questionStyles": {
                                    "selector": ".Skin .QuestionText",
                                    "styles": {
                                        "color": null,
                                        "fontFamily": "",
                                        "fontSize": "",
                                        "fontStyle": "",
                                        "fontWeight": "",
                                        "textDecoration": ""
                                        }
                                    },
                            "textEntryStyles": {
                                    "selector": ".Skin select, .Skin .InputText",
                                    "styles": {
                                        "color": null
                                        }
                                    },
                            "textStyles": {
                                    "selector": ".SkinInner",
                                    "styles": {
                                        "color": null,
                                        "fontFamily": "tahoma, geneva, sans-serif",
                                        "fontSize": null,
                                        "fontStyle": null,
                                        "fontWeight": null,
                                        "textDecoration": null
                                        }
                                    }
                            },
                "EOSMessage": "",
                "EOSMessageLibrary": "",
                "EOSRedirectURL": "http://",
                "EmailThankYou": "false",
                "ExternalCSS": null,
                "Footer": "",
                "Header": "<span style=\"font-size:19px;\"><span style=\"color: rgb(67, 70, 77);\">Olvasd el figyelmesen a mondatot. A f&eacute;lk&ouml;v&eacute;r sz&oacute; hely&eacute;re keress m&aacute;s sz&oacute;t, &uacute;gy, hogy a mondat jelent&eacute;se l&eacute;nyeg&eacute;ben ugyanaz maradjon. </span></span><br />\n<br />\n<span style=\"color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 19px;\">A sz&oacute;t abban az alakban &iacute;rd le, ahogy a mondatba ker&uuml;lne. Fontos, hogy csak egy sz&oacute; hely&eacute;re keres&uuml;nk jel&ouml;lteket, nagyobb mondatbeli egys&eacute;gek behelyettes&iacute;t&eacute;s&eacute;re ne tegy&eacute;l javaslatot, &eacute;s csak egy sz&oacute;b&oacute;l &aacute;ll&oacute; kifejez&eacute;st adj meg (&ouml;sszetett szavak j&ouml;hetnek).</span><br style=\"color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 19px;\" />\n<br />\n<span style=\"color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 19px;\">Mondatonk&eacute;nt legfeljebb &ouml;t sz&oacute;t javasolhatsz,&nbsp;</span><span style=\"color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 19px;\">e<span style=\"color: rgb(67, 70, 77);\">zeket &iacute;rd egym&aacute;s al&aacute; a sz&ouml;vegdobozba.</span>&Ouml;r&uuml;l&uuml;nk, ha nem &aacute;llsz meg egy jel&ouml;ltn&eacute;l.&nbsp;<span style=\"color: rgb(67, 70, 77);\">Ha nem jutna eszedbe j&oacute; sz&oacute;</span>, &aacute;ltal&aacute;nosabb jelent&eacute;s&#369; szavakat is megadhatsz (pl. &quot;k&ouml;rte&quot; helyett &quot;gy&uuml;m&ouml;lcs&quot;)<span style=\"color: rgb(67, 70, 77);\">, de lehet&#337;leg ne haszn&aacute;lj k&uuml;ls&#337; eszk&ouml;zt. K&eacute;s&#337;bb is visszat&eacute;rhetsz ehhez a mondathoz.</span></span><br />\n&nbsp;",
                "HighlightQuestions": "on",
                "InactiveMessage": "",
                "InactiveMessageLibrary": "",
                "InactiveSurvey": "DefaultMessage",
                "NewScoring": 1,
                "NextButton": "  >>  ",
                "NoIndex": "Yes",
                "PartialData": "+4 hour",
                "Password": "",
                "PasswordProtection": "No",
                "PreferJFE": false,
                "PreviousButton": "  <<  ",
                "ProgressBarDisplay": "NoText",
                "ProtectSelectionIds": true,
                "QuestionsPerPage": "1",
                "RefererCheck": "No",
                "RefererURL": "http://",
                "SaveAndContinue": "true",
                "ShowExportTags": "false",
                "Skin": "qtrial0",
                "SkinLibrary": "qtrial2014az1",
                "SkinType": "MQ",
                "SurveyExpiration": null,
                "SurveyMetaDescription": "Lexikális behelyettesítés",
                "SurveyProtection": "ByInvitation",
                "SurveyTermination": "DefaultMessage",
                "SurveyTitle": "Lexikális behelyettesítés",
                "ThankYouEmailMessage": null,
                "ThankYouEmailMessageLibrary": null,
                "ValidateMessage": "false",
                "ValidationMessage": null,
                "ValidationMessageLibrary": null,
                "footerMid": "",
                "headerMid": "",
                "libraryId": "",
                "nextButtonMid": "",
                "previousButtonMid": ""
            },
            "PrimaryAttribute": "Survey Options",
            "SecondaryAttribute": null,
            "SurveyID": "SV_6G3iaYPb3lqPJEV",
            "TertiaryAttribute": null
        },
        {
                "Element": "SCO",
                "Payload": {
                    "AutoScoringCategory": null,
                    "DefaultScoringCategory": null,
                    "ScoringCategories": [],
                    "ScoringCategoryGroups": [],
                    "ScoringSummaryAfterQuestions": 0,
                    "ScoringSummaryAfterSurvey": 0,
                    "ScoringSummaryCategory": null
                    },
                "PrimaryAttribute": "Scoring",
                "SecondaryAttribute": null,
                "SurveyID": "SV_6G3iaYPb3lqPJEV",
                "TertiaryAttribute": null
                },
        {
                "Element": "STAT",
                "Payload": {
                    "ID": "Survey Statistics",
                    "MobileCompatible": true
                    },
                "PrimaryAttribute": "Survey Statistics",
                "SecondaryAttribute": null,
                "SurveyID": "SV_6G3iaYPb3lqPJEV",
                "TertiaryAttribute": null
                },
        {
                "Element": "QC",
                "Payload": null,
                "PrimaryAttribute": "Survey Question Count",
                "SecondaryAttribute": "8",
                "SurveyID": "SV_6G3iaYPb3lqPJEV",
                "TertiaryAttribute": null
                },
        {
                "Element": "RS",
                "Payload": null,
                "PrimaryAttribute": "RS_9H9Bq526PLb02vH",
                "SecondaryAttribute": "Default Response Set",
                "SurveyID": "SV_6G3iaYPb3lqPJEV",
                "TertiaryAttribute": null
                },
        ],
    "SurveyEntry": {
            "CreatorID": "UR_d6GhZSAIuQ8mvgp",
            "Deleted": null,
            "DivisionID": null,
            "LastAccessed": "0000-00-00 00:00:00",
            "LastActivated": "0000-00-00 00:00:00",
            "LastModified": "2014-11-21 04:29:24",
            "SurveyActiveResponseSet": "RS_9H9Bq526PLb02vH",
            "SurveyBrandID": "qtrial2014az1",
            "SurveyCreationDate": "2014-11-21 03:59:18",
            "SurveyDescription": null,
            "SurveyExpirationDate": "0000-00-00 00:00:00",
            "SurveyID": "SV_6G3iaYPb3lqPJEV",
            "SurveyLanguage": "EN",
            "SurveyName": "Lexikális behelyettesítés",
            "SurveyOwnerID": "UR_d6GhZSAIuQ8mvgp",
            "SurveyStartDate": "0000-00-00 00:00:00",
            "SurveyStatus": "Inactive"
            }
    }

    for line in list(questions):
        try:
            (k, text) = line.split("\t")
        except:
            print repr(line.split("\t"))
        DataExportTag = "Q"+k
        QuestionID = "QID"+k
        QuestionText = text
        QuestionDescription = (QuestionText.split(" "))[:4]
        survey["SurveyElements"].append({
            "Element": "SQ",
            "Payload": {
                "Configuration": {
                    "InputHeight": 110,
                    "InputWidth": 200,
                    "QuestionDescriptionOption": "UseText"
                    },
                "DataExportTag": DataExportTag,
                "DefaultChoices": false,
                "GradingData": [],
                "Language": [],
                "QuestionDescription": QuestionDescription,
                "QuestionID": QuestionID,
                "QuestionText": QuestionText,
                "QuestionType": "TE",
                "Selector": "ML",
                "Validation": {
                    "Settings": {
                        "ForceResponse": "OFF",
                        "ForceResponseType": "ON",
                        "Type": "None"
                        }
                    }
                },
            "PrimaryAttribute": QuestionID,
            "SecondaryAttribute": QuestionDescription,
            "SurveyID": "SV_6G3iaYPb3lqPJEV",
            "TertiaryAttribute": null
            }
        )
        BL0.append({ "QuestionID": QuestionID, "Type": "Question" })
        BL0.append({ "Type": "Page Break" })

    return survey

if __name__ == "__main__":
    print json.dumps(qsf(sys.stdin.readlines()), indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False, encoding='utf-8').encode('utf-8')

