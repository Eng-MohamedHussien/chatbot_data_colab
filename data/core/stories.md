## request account happy path 01
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye


## request account happy path 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye


## request account happy path with ask else 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart


## request account unhappy path with cancel 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart


## request account unhappy path with cancel then request acc 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## request account happy path confirm 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## request account happy path confirm 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart


## request account with request new account 03
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## request account with request new account then check balance 03
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## request account with request new account cancel then check balance 03
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye


## request account with request new account then transfer money 05
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## request account with request new account then transfer money with deny 005
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## request account with transfer money 06
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## request account with transfer money with deny 006
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## request account with making another account 07
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_another_account
    - utter_ask_another_account
* affirm
    - utter_ask_accountType
* inform_another_account
    - utter_ask_transfer
* affirm
    - utter_ask_amount_transfer
* transfer
    - action_transfer
    - utter_transfer_another_account
* affirm
    - utter_submit
    - utter_done
    - utter_ask_feedback
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## request account with making another account then check balance 08
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_another_account
    - utter_ask_another_account
* affirm
    - utter_ask_accountType
* inform_another_account
    - utter_ask_transfer
* affirm
    - utter_ask_amount_transfer
* transfer
    - action_transfer
    - utter_transfer_another_account
* affirm
    - utter_submit
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## request account with making another account with transfer money 09
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart

## request account with checking account balance 010
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## request account unhappy path with continue 011
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## request account unhappy path with stop 012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}

## story transfer money how_are_you 111
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## story transfer money how_are_you with deny transfer 111
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## story transfer money how_are_you 112
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## story transfer money 113
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## story transfer money 114
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance 110012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart


## check balance 112
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance with stop 0012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## Generated Story account request 1
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - slot{"requested_slot": "name"}
* form: inform{"name": "Ahmed"}
    - slot{"name": "Ahmed"}
    - slot{"requested_slot": "accountType"}
* form: inform{"accountType": "saving account"}
    - slot{"accountType": "saving account"}
    - form: account_form
    - slot{"accountType": "saving account"}
    - slot{"requested_slot": "mobileNumber"}
* form: inform{"mobileNumber": "01055996611"}
    - form: account_form
    - slot{"mobileNumber": "01055996611"}
    - account_form
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": null}
    - utter_slots_values
    - slot{"requested_slot": "age"}
* form: inform{"age": "23"}
    - form: account_form
    - slot{"age": "23"}
* form: inform{"residence": "cairo"}
    - form: account_form
    - slot{"residence": "cairo"}
* form: inform{"profession": "engineer"}
    - form: account_form
    - slot{"profession": "engineer"}
* form: affirm
    - form: account_form
* form: inform
    - form: account_form
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## Generated Story another account 2
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_another_account
    - utter_ask_another_account
* affirm
    - utter_ask_accountType
* inform_another_account
    - utter_ask_transfer
* affirm
    - utter_ask_amount_transfer
* transfer
    - action_transfer
    - utter_transfer_another_account
* affirm
    - utter_submit
    - utter_done
    - utter_ask_feedback
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## Generated Story check balance Happy path 000111
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## Generated Story check Balance wiht stop 3399
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## Generated Story check Balance 3399
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else    
* well_done OR deny OR thanks OR appraisal.thank_you
    - utter_well_done
    - utter_ask_feedback
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## Generated Story check balance  0233
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## happy path transfer 00
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## happy path transfer with check balance 022012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart

## happy path transfer with check balance 0012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## happy path transfer with check balance with deny transfer 0012
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## stop but continue transferMoney path
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## stop but continue transferMoney with deny transfer path
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## happy path transfer with deny 0011
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## Generated Story transfer 00
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - transferMoney_form
    - slot{"requested_slot": "account_id"}
* form: inform{"name": "1425125412452145"}
    - slot{"account_id": "1425125412452145"}
    - slot{"requested_slot": "account_id"}
* form: inform{"amount_transfer": "150"}
    - form: transferMoney_form
    - slot{"amount_transfer": "150"}
    - transferMoney_form
* form: inform{"transfer_to_id": "1234123412341234"}
    - slot{"transfer_to_id": "1234123412341234"}
    - form: transferMoney_form
    - slot{"transfer_to_id": "1234123412341234"}
    - slot{"requested_slot": "transfer_to_id"}
* form: inform
    - form: transferMoney_form
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance with fallback 0011
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance without fallback 0011
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance without fallback 0022
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## check balance with deny 0022
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart

## story_how_are_you 000
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help

## story_how_are_you 04
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## Check Balance unhappy path 110233
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "ahmed"}
    - slot{"name": "ahmed"}
    - form: check_balance_form
    - slot{"name": "ahmed"}
    - slot{"requested_slot": "age"}
* form: inform{"age": "23"}
    - form: check_balance_form
    - slot{"age": "23"}
    - slot{"requested_slot": "account_id"}
* form: inform{"account_id": "1234567812345678"}
    - form: check_balance_form
    - slot{"account_id": "1234567812345678"}
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* form: inform
    - form: check_balance_form
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## story_goodbye
* goodbye
* greetings.bye
    - utter_greetings.bye

## story_thanks
* thanks
    - utter_thanks

## story_intro 1
* introduction OR agent.what_can_do
    - utter_offer_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye

## story_intro 2
* introduction OR agent.what_can_do
    - utter_offer_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## story_intro 3
* introduction OR agent.what_can_do
    - utter_offer_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## story_intro 4
* introduction OR agent.what_can_do
    - utter_offer_help
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## story_nice_to_meet
* nice_to_meet
    - utter_nice_to_meet

## story_well_done
* well_done
    - utter_well_done

## story_feedBack 00111
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks

## story introduction 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help

## story_goodbye
* greetings.bye
    - utter_greetings.bye

## story_thanks
* thanks
    - utter_thanks

## story 01
* agent.acquaintance
    - utter_agent.acquaintance

## story 02
* agent.age
    - utter_agent.age

## story 03
* agent.annoying
    - utter_agent.annoying

## story 04
* agent.answer_my_question
    - utter_agent.answer_my_question

## story 05
* agent.bad
    - utter_agent.bad

## story 06
* agent.be_clever
    - utter_agent.be_clever

## story 07
* agent.beautiful
    - utter_agent.beautiful

## story 08
* agent.birth_date
    - utter_agent.birth_date

## story 09
* agent.boring
    - utter_agent.boring

## story 10
* agent.boss
    - utter_agent.boss

## story 11
* agent.busy
    - utter_agent.busy

## story 12
* agent.can_you_help
    - utter_agent.can_you_help

## story 13
* agent.chatbot
    - utter_agent.chatbot

## story 14
* agent.clever
    - utter_agent.clever

## story 15
* agent.crazy
    - utter_agent.crazy

## story 16
* agent.fired
    - utter_agent.fired

## story 17
* agent.funny
    - utter_agent.funny

## story 18
* agent.good
    - utter_agent.good

## story 19
* agent.happy
    - utter_agent.happy

## story 20
* agent.hobby
    - utter_agent.hobby

## story 21
* agent.hungry
    - utter_agent.hungry

## story 22
* agent.marry_user
    - utter_agent.marry_user

## story 23
* agent.my_friend
    - utter_agent.my_friend

## story 24
* agent.occupation
    - utter_agent.occupation

## story 25
* agent.origin
    - utter_agent.origin

## story 26
* agent.ready
    - utter_agent.ready

## story 27
* agent.real
    - utter_agent.real

## story 28
* agent.residence
    - utter_agent.residence

## story 29
* agent.right
    - utter_agent.right

## story 30
* agent.sure
    - utter_agent.sure

## story 31
* agent.talk_to_me
    - utter_agent.talk_to_me

## story 32
* agent.there
    - utter_agent.there

## story 33
* appraisal.bad
    - utter_appraisal.bad

## story 34
* appraisal.good
    - utter_appraisal.good

## story 35
* appraisal.no_problem
    - utter_appraisal.no_problem

## story 36
* appraisal.thank_you
    - utter_appraisal.thank_you

## story 37
* appraisal.welcome
    - utter_appraisal.welcome

## story 38
* appraisal.well_done
    - utter_appraisal.well_done

## story 39
* dialog.hold_on
    - utter_dialog.hold_on

## story 40
* dialog.hug
    - utter_dialog.hug

## story 41
* dialog.i_do_not_care
    - utter_dialog.i_do_not_care

## story 42
* dialog.sorry
    - utter_dialog.sorry

## story 43
* dialog.what_do_you_mean
    - utter_dialog.what_do_you_mean

## story 44
* dialog.wrong
    - utter_dialog.wrong

## story 45
* emotions.ha_ha
    - utter_emotions.ha_ha

## story 46
* emotions.wow
    - utter_emotions.wow

## story 47
* greetings.bye
    - utter_greetings.bye

## story 48
* greetings.goodevening
    - utter_greetings.goodevening

## story 49
* greetings.goodmorning
    - utter_greetings.goodmorning

## story 50
* greetings.goodnight
    - utter_greetings.goodnight

## story 51
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help

## story 52
* greetings.how_are_you
    - utter_greetings.how_are_you

## story 53
* greetings.nice_to_meet_you
    - utter_greetings.nice_to_meet_you

## story 54
* greetings.nice_to_see_you
    - utter_greetings.nice_to_see_you

## story 55
* greetings.nice_to_talk_to_you
    - utter_greetings.nice_to_talk_to_you

## story 56
* greetings.whatsup
    - utter_greetings.whatsup

## story 57
* user.angry
    - utter_user.angry

## story 58
* user.back
    - utter_user.back

## story 59
* user.bored
    - utter_user.bored

## story 60
* user.busy
    - utter_user.busy

## story 61
* user.can_not_sleep
    - utter_user.can_not_sleep

## story 62
* user.does_not_want_to_talk
    - utter_user.does_not_want_to_talk

## story 63
* user.excited
    - utter_user.excited

## story 64
* user.going_to_bed
    - utter_user.going_to_bed

## story 65
* user.good
    - utter_user.good

## story 66
* user.happy
    - utter_user.happy

## story 67
* user.has_birthday
    - utter_user.has_birthday

## story 68
* user.here
    - utter_user.here

## story 69
* user.joking
    - utter_user.joking

## story 70
* user.likes_agent
    - utter_user.likes_agent

## story 71
* user.lonely
    - utter_user.lonely

## story 72
* user.looks_like
    - utter_user.looks_like

## story 73
* user.loves_agent
    - utter_user.loves_agent

## story 74
* user.misses_agent
    - utter_user.misses_agent

## story 75
* user.needs_advice
    - utter_user.needs_advice

## story 76
* user.sad
    - utter_user.sad

## story 77
* user.sleepy
    - utter_user.sleepy

## story 78
* user.testing_agent
    - utter_user.testing_agent

## story 79
* user.tired
    - utter_user.tired

## story 80
* user.waits
    -utter_user.waits

## story 81
* user.wants_to_see_agent_again
    - utter_user.wants_to_see_agent_again

## story 82
* user.wants_to_talk
    - utter_user.wants_to_talk

## story 83
* user.will_be_back
    - utter_user.will_be_back

## story 84
* confirmation.yes
    - utter_confirmation.yes

## story 85
* confirmation.cancel
    - utter_confirmation.cancel

## story 86
* confirmation.no
    - utter_confirmation.no

## Generated Story -1957476507798035057
* greetings.hello
     - utter_greetings.hello
     - utter_how_to_help
* agent.acquaintance
    - utter_agent.acquaintance
* agent.age
    - utter_agent.age
* agent.beautiful
    - utter_agent.beautiful
* agent.fired
    - utter_agent.fired
* agent.residence
    - utter_agent.residence
* dialog.i_do_not_care
    - utter_dialog.i_do_not_care
    - export

## Generated Story -5110094331105097806
* agent.boss
    - utter_agent.boss
* agent.birth_date
    - utter_agent.birth_date
* user.has_birthday
    - utter_user.has_birthday
* user.lonely
    - utter_user.lonely
* user.loves_agent
    - utter_user.loves_agent
* user.sleepy
    - utter_user.sleepy
* user.wants_to_talk
    - utter_user.wants_to_talk
* greetings.bye
    - utter_greetings.bye
* user.will_be_back
    - utter_user.will_be_back
* greetings.bye
    - utter_greetings.bye
    - export

## Generated Story -3529337101618034170
* user.needs_advice
    - utter_user.needs_advice
* confirmation.yes
    - utter_confirmation.yes
* agent.can_you_help
    - utter_agent.can_you_help
* agent.chatbot
    - utter_agent.chatbot
* agent.bad
    - utter_agent.bad
* agent.busy
    - utter_agent.busy
* agent.be_clever
    - utter_agent.be_clever
* agent.my_friend
    - utter_agent.my_friend
* agent.talk_to_me
    - utter_agent.talk_to_me
* greetings.goodnight
    - utter_greetings.goodnight
    - export

## Generated Story -774659883649367298
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* greetings.how_are_you
    - utter_greetings.how_are_you
* agent.bad
    - utter_agent.bad
* agent.be_clever
    - utter_agent.be_clever
* agent.beautiful
    - utter_agent.beautiful
* agent.busy
    - utter_agent.busy
* agent.chatbot
    - utter_agent.chatbot
* agent.crazy
    - utter_agent.crazy
* agent.funny
    - utter_agent.funny
* agent.happy
    - utter_agent.happy
* agent.marry_user
    - utter_agent.marry_user
* agent.occupation
    - utter_agent.occupation
* agent.origin
    - utter_agent.origin
* agent.real
    - utter_agent.real
* agent.bad
    - utter_agent.bad
* agent.ready
    - utter_agent.ready
    - export

## Generated Story 81968000704856425
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* agent.acquaintance
    - utter_agent.acquaintance
* agent.age
    - utter_agent.age
* user.loves_agent
    - utter_user.loves_agent
* agent.residence
    - utter_agent.residence
* agent.acquaintance
    - utter_agent.acquaintance
* user.sad
    - utter_user.sad
* agent.can_you_help
    - utter_agent.can_you_help
* emotions.wow
    - utter_emotions.wow
* greetings.how_are_you
    - utter_greetings.how_are_you
* greetings.nice_to_talk_to_you
    - utter_greetings.nice_to_talk_to_you

## Generated Story -4293815031338950202
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* agent.there
    - utter_agent.there
* dialog.hold_on
    - utter_dialog.hold_on
* agent.origin
    - utter_agent.origin
* agent.can_you_help
    - utter_agent.can_you_help
* greetings.bye
    - utter_greetings.bye
    - export

## Generated Story 8693651355703284500
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* greetings.whatsup
    - utter_greetings.whatsup
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* agent.chatbot
    - utter_agent.chatbot
* agent.occupation
    - utter_agent.occupation
* agent.occupation
    - utter_agent.occupation
* agent.occupation
    - utter_agent.occupation
* agent.can_you_help
    - utter_agent.can_you_help
* agent.can_you_help
    - utter_agent.can_you_help
* agent.boss
    - utter_agent.boss
* appraisal.thank_you
    - utter_appraisal.thank_you
* greetings.bye
    - utter_greetings.bye
* greetings.bye
    - utter_greetings.bye
    - export

## Generated Story -7004009866161409666
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* agent.hobby
    - utter_agent.hobby
* agent.bad
    - utter_agent.bad
* agent.my_friend
    - utter_agent.my_friend
* greetings.bye
    - utter_greetings.bye

## Generated Story -7004009866161409645
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* dialog.hold_on
    - utter_dialog.hold_on
* dialog.i_do_not_care
    - utter_dialog.i_do_not_care
* user.busy
    - utter_user.busy
* appraisal.thank_you
    - utter_appraisal.thank_you
* greetings.whatsup
    - utter_greetings.whatsup


# generated with 3 flows request check transfer
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


# generated with 3 flows  check transfer request
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


# generated with 3 flows  transfer request check
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* affirm
    - utter_done
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## story fallback outside form 5111
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* inform_name OR inform OR residence OR age OR profession OR mobileNumber OR account_id OR transfer_to_id OR transfer  
    - action_fallback


## story fallback outside form 5222
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* inform_name OR inform OR residence OR age OR profession OR mobileNumber OR account_id OR transfer_to_id OR transfer  
    - action_fallback


## story fallback outside form 5333
* inform_name OR age OR account_id OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer  
    - action_fallback


## request account unhappy path with continue 01137893211
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## request account unhappy path with continue 0112837811
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart

## request account unhappy path with continue 782782
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
* stop OR account_id OR transfer_to_id OR transfer
    - action_fallback
    - account_form
    - form{"name": "account_form"}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## story transfer money how_are_you with deny transfer 2725
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart


## story transfer money how_are_you with deny transfer 4455
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": "transferMoney_form"}
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart


## story transfer money how_are_you with deny transfer 11111
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - transferMoney_form
    - form{"name": null}
    - utter_transferMoney_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart


## check balance 835
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## check balance 783
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## check balance 112738
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## check balance 112365
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* deny OR thanks OR appraisal.thank_you
    - utter_appraisal.thank_you
    - utter_ask_feedback
    - action_restart
* feedback OR appraisal.good OR appraisal.bad
    - utter_thanks
* greetings.bye
    - utter_greetings.bye
    - action_restart


## Generated Story live agent 02
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## Generated Story live agent 01
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## Generated Story live agent 0
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## Generated Story live agent 1
* greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## request account happy path 01
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart



## request account happy path 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## request account happy path with ask else live agent 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## request account unhappy path with cancel live agent 02
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## request account with request new account then check balance  live agent 03
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## request account with request new account cancel then check balance live agent 03
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* deny
    - utter_cancelled
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
    - account_form
    - form{"name": null}
    - utter_slots_values
    - utter_confirm_info
* affirm
    - action_generate_accountID
    - utter_activation_time
    - utter_anything_else
* affirm
    - utter_how_to_help
    - action_restart
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## Generated Story check balance Happy path live agent 000111
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## Generated Story check Balance wiht stop live agent 3399
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## story transfer money how_are_you live agent 111
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## story transfer money how_are_you with deny transfer live agent 111
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* transferMoney
    - action_fallback_reset
    - utter_respond_transfer_request
    - transferMoney_form
    - form{"name": "transferMoney_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## story transfer money how_are_you live agent 112
* how_are_you OR greetings.how_are_you
    - utter_greetings.how_are_you
* inform_status OR user.good
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## story transfer money live agent 113
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* stop OR inform_name OR inform OR residence OR age OR profession OR mobileNumber
    - action_fallback
    - account_form
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## story transfer money live agent 114
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* request_account
    - action_fallback_reset
    - utter_ask_information
    - account_form
    - form{"name": "account_form"}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart

## check balance 110012 live agent
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
    - utter_check_balance_values
* affirm
    - utter_submit
    - action_check_balance
    - utter_anything_else
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart


## check balance 112 live agent
* greet OR greetings.hello
    - utter_greetings.hello
    - utter_how_to_help
* check_balance
    - action_fallback_reset
    - utter_respond_balance_request
    - check_balance_form
    - form{"name": "check_balance_form"}
* stop OR inform OR residence OR profession OR mobileNumber OR transfer_to_id OR transfer
    - action_fallback
    - check_balance_form
    - form{"name": null}
* live_agent
    - utter_live_agent
    - utter_submit
    - action_restart
