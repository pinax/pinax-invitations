.. _usage:

Usage
=====

Integrating `kaelo` into your project is just a matter of using a couple of
template tags and wiring up a bit of javascript. The invite form is intended
to function via AJAX and as such returns JSON.

Firstly, you will want to add the following blocks in your templates where
you want to expose the invite form and display to the user a list of who they
have invited (of course you may choose to not expose that):

.. code-block: django
    
    {% load kaleo_tags %}
    
    <div class="invites">
        {% invite_form request.user %}
        
        <div class="sent">
            <h3>Invitations Sent</h3>
            {% invites_sent request.user %}
        </div>
    </div>


Then if you had an account bar somewhere at the top of your screen where you
showed the user if they were logged in or note you could have:

.. code-block: django
    
    {% load kaleo_tags %}
    
    <span class="invitations_remaining">
        ({% remaining_invites user %})
    </span>


And then a bit of jQuery:

.. code-block: javascript
    
    $(function () {
        $('.invites form').ajaxForm(function(data) {
            if (data.status == "OK") {
                $('#invitation-form-messages').html("<p>Invitation sent to " + data.email + "</p>");
                $('.empty-invites').remove();
                $('.invite-list').append("<li>" + data.email + "</li>");
                $('.invites form input[type=text]').val("");
                $('.invitations_remaining').html("(" + data.invitations_remaining + ")");
                if (data.invitations_remaining == 0) {
                    $('.invitation_form form').hide();
                }
            } else {
                $('#invitation-form-messages').html(data.errors);
            }
        });
    });
