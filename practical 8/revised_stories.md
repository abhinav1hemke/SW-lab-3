# Revised User Stories

## US-01: Register an account

**Requirement:** REQ-01

**As a** visitor, **I want** to register with my email and password, **so that**
I can create an account and use the portal.

### Acceptance criteria

- Given my email is not registered and my password has at least eight characters, When I submit valid registration details, Then my account is created and a success confirmation is displayed.
- Given my email is already registered, When I submit the registration form, Then the system rejects the registration and explains that the email is unavailable.

## US-02: Sign in and sign out

**Requirement:** REQ-02

**As a** registered user, **I want** to sign in and sign out, **so that** I can
access my account and end my session when finished.

### Acceptance criteria

- Given I enter my registered email and correct password, When I submit the sign-in form, Then I am signed in and can access my account.
- Given I enter an incorrect email or password, When I submit the sign-in form, Then the system displays an invalid-credentials error and does not sign me in.
- Given I am signed in, When I choose to sign out, Then my session ends and protected account content is no longer available.

## US-03: Request a password reset

**Requirement:** REQ-03

**As a** registered user, **I want** to request a password reset by email, **so that** I can regain access if I forget my password.

### Acceptance criteria

- Given I enter an email address registered to an account, When I submit a reset request, Then the system confirms the request without displaying account credentials.
- Given I enter an email address not registered to an account, When I submit a reset request, Then the system displays the same confirmation as for a registered email.
