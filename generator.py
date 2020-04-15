def generate_group(groups, domain, out_file):
    """
        dn: cn=test_group,cn=users,dc=logpoint,dc=local
        cn: test_group
        objectClass: top
        objectClass: group
    """
    out_string=[]
    for group_name in groups:
        out_string.append(
f"""dn: cn={group_name},cn=users,dc={domain[0]},dc={domain[1]}
cn: {group_name}
objectClass: top
objectClass: group
\n""")

    with open(out_file, 'w') as fp:
        fp.writelines(out_string)

def generate_member(group_user_tracking, domain, out_file):
    """
        dn: cn=Ossama Griffith,cn=Users,dc=logpoint,dc=local
        objectClass: top
        objectClass: person
        objectClass: organizationalPerson
        objectClass: user
        cn: Ossama Griffith
        sn: Griffith
        sAMAccountName: GriffitO
        userPassword: Password1
        givenName: Ossama
    """
    out_string = []
    for group in group_user_tracking:
        for user, sn in group_user_tracking[group]:
            out_string.append(
f"""dn: cn={user} {sn},cn=Users,dc={domain[0]},dc={domain[1]}
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: {user} {sn}
sn: {sn}
sAMAccountName: {(user+sn).replace(' ', '')[:18]}0
userPassword: Password1
givenName: {sn}
\n""")

    with open(out_file, 'a') as fp:
        fp.writelines(out_string)

def finalize_members(group_user_tracking, domain, out_file):
    """
        dn: cn=test_group,cn=users,dc=logpoint,dc=local
        changetype: modify
        add: member
        member: cn=Ossama Griffith,cn=Users,dc=logpoint,dc=local
        member: cn=Ram Khanal,cn=Users,dc=logpoint,dc=local
        member: cn=Hari Poudel,cn=Users,dc=logpoint,dc=local
    """
    out_string = []
    for group in group_user_tracking:
        group_string = ""
        for user, sn in group_user_tracking[group]:
            group_string += f"member: cn={user} {sn},cn=Users,dc={domain[0]},dc={domain[1]}\n"
        out_string.append(
f"""dn: cn={group},cn=users,dc={domain[0]},dc={domain[1]}
changetype: modify
add: member
{group_string}-

""")

    with open(out_file, 'a') as fp:
        fp.writelines(out_string)


