# BUG-001: Empty username does not prevent login submission

**Severity:** Medium  
**Priority:** P2  
**Status:** Verified / Closed  
**Environment:** Chrome 120, Windows 11, saucedemo.com

## Steps to Reproduce

1. Navigate to https://www.saucedemo.com
2. Leave username field empty
3. Leave password field empty
4. Click "Login"

## Expected

Inline validation prevents submission; user sees field-level error.

## Actual

Form submits; error banner shown: "Username is required".

## Root Cause

Client-side validation missing on empty submit.

## Fix Verification

Retested after fix — error banner displays immediately. Automated in `test_login.py::test_empty_credentials`.
