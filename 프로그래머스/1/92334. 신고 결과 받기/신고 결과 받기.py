def solution(id_list, report, k):
    report = list(set(report))
    report_count = {user: 0 for user in id_list}
    user_reports = {user: [] for user in id_list}
    
    for cmd in report:
        reporter, reportee = cmd.split()
        if reportee not in user_reports[reporter]:
            user_reports[reporter].append(reportee)
            report_count[reportee] += 1
            
    suspended_users = [user for user, count in report_count.items() if count >= k]
    
    mail_count = {user: 0 for user in id_list}
    
    for reporter in id_list:
        for reportee in user_reports[reporter]:
            if reportee in suspended_users:
                mail_count[reporter] += 1
                
    return [mail_count[user] for user in id_list]