# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

import logging
import requests
import json
import random
from rasa_core_sdk import Action
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted
from random import randint
import re
import pandas as pd
from rasa_core_sdk.events import UserUtteranceReverted


from rasa_core_sdk.events import FollowupAction
from rasa_core_sdk.events import ConversationPaused

#rasa_core.trackers

print("starting actions ")
fallback_num = 0
fallback_num_inside_form = 0
lsts= []
names = []
name = ""
OTP = str(999999)
try_OTP_counts = 0


class ActionFallbackReset(Action):
    def name(self):
        return 'action_fallback_reset'
    def run(self, dispatcher, tracker, domain):
        global fallback_num_inside_form
        global fallback_num
        global name
        name = ""
        fallback_num_inside_form = 0
        fallback_num = 0
        return []


def get_names(fileName):
    global names
    #to get all names from the dataset
    data = pd.read_csv(fileName)
    for i in range (len(data['candidate_name'])):
        name = data['candidate_name'][i]
        name = re.sub('[.)(/?-]'," ",name)
        name = name.split(" ")
        for n in name:
            if len(n) > 2 :
                names.append(n)
    names = list(set(names))

get_names("valid_names.csv")

def generate_id(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


class ActionDefaultFallback(Action):
#Executes the fallback action and goes back to the previous state
    #of the dialogue

    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):

        global fallback_num_inside_form
        global fallback_num
        #global fallback_counts
        #intent =  tracker.latest_message['intent'].get('name')
        #print("----INTENT-----",intent)

        #latest_action =  tracker.latest_action_name
        #print("----latest _ action -----",latest_action)

        #latest_message =  tracker.latest_message
        #print("---- latest_message -----",latest_message)

        #followup_action =  tracker.followup_action
        #print("----followup_action -----",followup_action)
        requested_slt = tracker.get_slot("requested_slot")
        #latest_entity_values = tracker.get_latest_entity_values("requested_slot")
        #current_state = tracker.current_state()
        current_slot_values = tracker.current_slot_values()
        #print("latest_entity_values",latest_entity_values,"current_state",current_state,"current_slot_values",current_slot_values)
        print("requested_slot",requested_slt)
        print("current_slot_values",current_slot_values)

        active_form =  tracker.active_form
        print("---- active_form -----",active_form)
        if active_form:
            #INSIDE FORM FALLBACK
            active_form_name = active_form['name']
            print("---- In active form ==>",active_form_name)
            fallback_num_inside_form += 1
            if fallback_num_inside_form == 5:

                print("....... INside form COUNTS ===> 3 .......")
                dispatcher.utter_template("utter_exceed_fallback", tracker,
                                      silent_fail=True)
                dispatcher.utter_template("utter_submit", tracker,
                                      silent_fail=True)
                fallback_num_inside_form = 0
                return [ConversationPaused()]
            else:
                if requested_slt == 'age':
                    dispatcher.utter_message("Age is not valid or not allowed, please try again.")
                elif requested_slt == 'mobileNumber':
                    dispatcher.utter_message("Mobile number is incorrect, please try again")
                elif requested_slt == 'accountType':
                    dispatcher.utter_template("utter_wrong_accountType", tracker,silent_fail=True)
                #elif requested_slt == 'name':
                #    dispatcher.utter_message("")
                elif requested_slt == 'OTP':
                    dispatcher.utter_message("OTP is incorrect. Please try again")
                elif requested_slt == 'account_id':
                    dispatcher.utter_template("utter_wrong_account_id", tracker,silent_fail=True)
                elif requested_slt == 'amount_transfer':
                    dispatcher.utter_message("It's a wrong amount, Please enter an amount from 50 to 2000 with the currency of the transaction.")
                #elif requested_slt == 'residence':
                #    dispatcher.utter_message("")
                elif requested_slt == 'transfer_to_id':
                    dispatcher.utter_template("utter_wrong_account_id", tracker,silent_fail=True)
                #elif requested_slt == 'profession':
                #    dispatcher.utter_message("")
                elif requested_slt == 'general_account_id':
                    dispatcher.utter_template("utter_wrong_account_id", tracker,silent_fail=True)
            return [(FollowupAction(active_form_name))]

        else:
            # OUTSIDE FORM FALLBACK
            fallback_num += 1
            if fallback_num == 5:
                print("....... IN COUNTS 3 .......")
                dispatcher.utter_template("utter_exceed_fallback", tracker,
                                      silent_fail=True)
                dispatcher.utter_template("utter_submit", tracker,
                                      silent_fail=True)
                fallback_num = 0
            else:
                dispatcher.utter_template("utter_default", tracker,silent_fail=True)
                dispatcher.utter_template("utter_offer_help", tracker, silent_fail=True)

        #if not active_form :
        #    dispatcher.utter_template("utter_offer_help", tracker, silent_fail=True)
        #    return [UserUtteranceReverted()]

        return ()



class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'
    def run(self, dispatcher, tracker, domain):
        return[Restarted()]

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]


class ActionGenerateID(Action):
    def name(self):
        return 'action_generate_accountID'
    def run(self, dispatcher, tracker, domain):
        generated_id = generate_id(16)
        generated_id_msg = ""
        print(generated_id)
        generated_id_msg = "Your account id is  "+str(generated_id)
        print(generated_id_msg)

        # utter submit template
        #dispatcher.utter_template('utter_submit', tracker)
        dispatcher.utter_message(generated_id_msg)
        return[]


class ActionTransfer(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_transfer"

    def run(self, dispatcher, tracker, domain):
        amount_transfer = tracker.get_slot('amount_transfer')
        print("amount_transfer : ",amount_transfer)
        dispatcher.utter_message(" Transfering amount =  "+amount_transfer+" To The new account ")




class ActionCheckBalance(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        balance = random.randint(10,1000)
        balance = str(balance)
        account_id = tracker.get_slot('account_id')
        if account_id == None:
            dispatcher.utter_template('utter_wrong_account_id',
                                  tracker)

        account_id = str(account_id)
        #print(account_id,type(account_id))
        dispatcher.utter_message(" Your debit balance is "+balance + " USD")

class AccountForm(FormAction):
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "account_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["name", "age", "residence", "profession", "mobileNumber","accountType"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"name": [self.from_entity(entity="name",intent="inform_name"),self.from_entity(entity="name")],
                "accountType": [self.from_entity(entity="accountType",intent="inform"),self.from_entity(entity="accountType")],
                "residence": [self.from_entity(entity="residence",intent="residence"),self.from_entity(entity="residence")],
                "age": [self.from_entity(entity="age",intent="age"),self.from_entity(entity="age")],
                "profession": self.from_entity(entity="profession",intent="profession"),
                "mobileNumber": [self.from_entity(entity="mobileNumber",intent="mobileNumber"),
                               self.from_entity(entity="mobileNumber")]}

    @staticmethod
    def accountType_db():
        # type: () -> List[Text]
        """Database of supported accounts"""
        return ["saving account",
                "recurring account",
                "fixed deposit account",
                "current account"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity

        #print("Fall back count in Account form after reseting",fallback_counts)

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances

        for slot, value in slot_values.items():

            #if slot == 'name':
            #    if value.lower() not in self.clientNames_db():
            #        dispatcher.utter_template('utter_wrong_name', tracker)
                    # validation failed, set slot to None
            #        slot_values[slot] = None

            if slot == 'accountType':
                if value.lower() not in self.accountType_db():
                    dispatcher.utter_template('utter_wrong_accountType', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                else:
                    value = value.capitalize()
                    slot_values[slot] = value

            elif slot == 'mobileNumber':

                print(value,type(value))
                value = re.sub(r'(\d)\s+(\d)', r'\1\2',value)
                print(value)
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_mobileNumber',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                elif len(value) > 12 or len(value) < 9 :
                    dispatcher.utter_template('utter_wrong_mobileNumber',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                else:
                    slot_values[slot] = value

            elif slot == 'residence':
                value = value.capitalize()
                slot_values[slot] = value


            elif slot == 'age':
                if not self.is_int(value) or int(value) <= 0 or int(value) > 150 or int(value) < 15:
                    dispatcher.utter_template('utter_wrong_age',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'profession':
                value = value.capitalize()
                slot_values[slot] = value


            elif slot == 'name':
                global name
                slot_values[slot] = name
                logging.debug('name =======>'+str(name))
                if not name:     # if name is empty

                    #logging.debug('slot_values[slot] =======>' +str(slot_values[slot]))
                    #logging.debug('Names in dataset =======>' +str(names))
                    #print('Names in dataset =======>',names)
                    value = value.capitalize()
                    if value not in names:
                        dispatcher.utter_template('utter_ask_rephrase', tracker)
                        # validation failed, set slot to None
                        if name:
                            slot_values[slot] = name
                        else:
                            slot_values[slot] = None

                    else:
                        #value = value.capitalize()
                        slot_values[slot] = value
                        name = value
                        #print(name,value)
                        dispatcher.utter_message("Welcome "+name)


        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        #dispatcher.utter_template('utter_slots_values', tracker)
        #dispatcher.utter_template('utter_confirm_info', tracker)
        return []


class transferMoneyForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "transferMoney_form"

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name","account_id", "amount_transfer", "transfer_to_id"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"name": [self.from_entity(entity="name",intent="inform_name"),self.from_entity(entity="name")],
                "account_id":  [self.from_entity(entity="account_id",intent= "account_id"),
                               self.from_entity(entity="general_account_id")],
                "transfer_to_id": [self.from_entity(entity="transfer_to_id",
                                                intent= "transfer_to_id"),
                               self.from_entity(entity="general_account_id")],
                "amount_transfer": [self.from_entity(entity="amount_transfer", intent="transfer"),
                               self.from_entity(entity="amount_transfer")]}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity

        #intent =  tracker.latest_message['intent'].get('name')
        #print("----INTENT-----",intent)


        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances

        for slot, value in slot_values.items():

            #if slot == 'name':
            #    if value.lower() not in self.clientNames_db():
            #        dispatcher.utter_template('utter_wrong_name', tracker)
                    # validation failed, set slot to None
            #        slot_values[slot] = None


            if slot == 'account_id':
                value = re.sub(r'(\d)\s+(\d)', r'\1\2',value)
                if not self.is_int(value) or int(value) <= 0 or len(value) != 16:
                    dispatcher.utter_template('utter_wrong_account_id',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                else:
                    slot_values[slot] = value

            elif slot == 'transfer_to_id':
                value = re.sub(r'(\d)\s+(\d)', r'\1\2',value)
                if not self.is_int(value) or int(value) <= 0 or len(value) != 16:
                    dispatcher.utter_template('utter_wrong_account_id',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                else:
                    slot_values[slot] = value


            elif slot == 'amount_transfer':
                if not self.is_int(value) or int(value) <= 0 :
                    dispatcher.utter_template('utter_wrong_amount_transfer',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                if int(value) > 2000 or int(value) < 50 :
                	dispatcher.utter_message("Wrong amount, Please enter amount with minimum limit 50 and maximum limit 2000.")
                	slot_values[slot] = None


            elif slot == 'name':
                global name
                slot_values[slot] = name
                #logging.debug('name =======>'+str(name))
                if not name:     # if name is empty

                    #logging.debug('slot_values[slot] =======>' +str(slot_values[slot]))
                    #logging.debug('Names in dataset =======>' +str(names))
                    #print('Names in dataset =======>',names)
                    value = value.capitalize()
                    if value not in names:
                        dispatcher.utter_template('utter_ask_rephrase', tracker)
                        # validation failed, set slot to None
                        if name:
                            slot_values[slot] = name
                        else:
                            slot_values[slot] = None

                    else:
                        #value = value.capitalize()
                        slot_values[slot] = value
                        name = value
                        #print(name,value)
                        dispatcher.utter_message("Welcome "+name)

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict]:

           # utter submit template
           dispatcher.utter_template('utter_submit', tracker)
           #dispatcher.utter_template('utter_transferMoney_values', tracker)
           return []


class check_balanceForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "check_balance_form"

    '''@staticmethod
    def clientNames_db():
        # type: () -> List[Text]
        """Database of supported clients"""
        return ["ahmed",
                "david",
                "sam",
                "juste"]'''

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False
    @staticmethod

    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name","age","account_id"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"name": [self.from_entity(entity="name",intent="inform_name"),self.from_entity(entity="name")],
                "account_id": [self.from_entity(entity="account_id", intent="account_id"),
                                self.from_entity(entity="general_account_id", intent="general_account_id"),    
                                self.from_entity(entity="general_account_id")],
                "age": [self.from_entity(entity="age",intent="age"),self.from_entity(entity="age")]}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances

        for slot, value in slot_values.items():
            if slot == 'name':
                    #logging.debug('Names in dataset =======>' +str(names))
                    #print('Names in dataset =======>',names)
                    value = value.capitalize()
                    if value not in names:
                        dispatcher.utter_template('utter_wrong_name', tracker)
                        # validation failed, set slot to None
                        slot_values[slot] = None
                    else:
                        value = value.capitalize()
                        slot_values[slot] = value

            elif slot == 'account_id':
                value = re.sub(r'(\d)\s+(\d)', r'\1\2',value)
                print("ACCOUNT ID SAVED => "+value)
                if not self.is_int(value) or int(value) <= 0 or len(value) != 16:
                    dispatcher.utter_template('utter_wrong_account_id',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
                else:
                    slot_values[slot] = value

            elif slot == 'age':
                if not self.is_int(value) or int(value) <= 0 or int(value) > 150 or int(value) < 15:
                    dispatcher.utter_template('utter_wrong_age',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None


        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict]:

           # utter submit template
           print(tracker.get_slot('name'))
           dispatcher.utter_template('utter_submit', tracker)
           #dispatcher.utter_template('utter_check_balance_values', tracker)
           return []

class check_OTPForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "check_OTP_form"

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer  True = integer """
        try:
            int(string)
            return True
        except ValueError:
            return False
    @staticmethod

    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["OTP"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"OTP": [self.from_entity(entity="OTP",intent="inform_OTP"),self.from_entity(entity="OTP")]}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            global try_OTP_counts
            if slot == 'OTP':
                checking_otp = int(value)
                print("OTP : "+str(OTP),"checking OTP : "+str(checking_otp))
                #print(self.is_int(value),"   ",len(value),"   ", len(value))
                if not self.is_int(value) or len(value) <= 0 or len(value) > 6:
                    dispatcher.utter_message('OTP is incorrect. Please try again ')
                    try_OTP_counts += 1
                    slot_values[slot] = None
                    if try_OTP_counts > 4 :
                        #print("EXCEEDED 1")
                        dispatcher.utter_message('You have exceeded the number of tries. Try again later.')
                        slot_values[slot] = None
                        return []  
                else:
                    print("IN ELSE")
                    if checking_otp == int(OTP):
                        print("MATCHED")
                        dispatcher.utter_message('Transaction completed successfully')
                        slot_values[slot] = value
                        return [SlotSet(slot, value) for slot, value in slot_values.items()]
                    else:
                        dispatcher.utter_message('OTP is incorrect. Please try again ')
                        try_OTP_counts += 1
                        print("Number of tries OTP "+str(try_OTP_counts))
                        if try_OTP_counts < 3 :
                            slot_values[slot] = None
                        else:
                            dispatcher.utter_message('You have exceeded the number of tries .')
                            dispatcher.utter_message(' ...Transaction canceled...')
                            slot_values[slot] = "000000"

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict]:

           # utter submit template
           #dispatcher.utter_template('utter_submit', tracker)
           #dispatcher.utter_template('utter_check_balance_values', tracker)
           return []




'''class ActionCheck_OTP(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_check_OTP"

    def run(self, dispatcher, tracker, domain):
        #try_counts = 0
        OTP = str(999999)
        check_otp = tracker.get_slot('OTP')

        print("OTP IS : "+str(OTP),"Checking OTP :"+str(check_otp))
        print("Number of tries : "+str(try_counts))
        if int(check_otp) == int(OTP):
            dispatcher.utter_message('Transaction completed successfully')
        else:
            dispatcher.utter_message('OTP is incorrect. Transaction canceled ')
            try_counts += 1
            if try_counts < 3 :
                dispatcher.utter_message('OTP is incorrect. Transaction canceled ')
                dispatcher.utter_template('utter_OTP',tracker)
                for slot in tracker.slots:
                    if slot == "OTP":
                        SlotSet(slot, None)
                return FollowupAction("action_check_OTP")

            else:
                return UserUtteranceReverted()
        return ()'''


####### Reset all slot except One ######
#return_slots = []
#for slot in tracker.slots:
#    if slot != "foo":
#        return_slots.append(SlotSet(slot, None))
#return return_slots
