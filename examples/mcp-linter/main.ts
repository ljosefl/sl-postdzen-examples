import * as fs from 'fs';
import * as path from 'path';
import * as childProcess from 'child_process';

interface HealthCheckResult {
    grade: string;
    score: number;
    issues: string[];
}

function checkConsoleLogs(filePath: string): boolean {
    const content = fs.readFileSync(filePath, 'utf-8');
    return content.includes('console.log');
}

function checkDestructiveHint(filePath: string): boolean {
    const content = fs.readFileSync(filePath, 'utf-8');
    return !content.includes('// destructiveHint: true');
}

function checkPromptInjection(filePath: string): boolean {
    const content = fs.readFileSync(filePath, 'utf-8');
    return content.includes('prompt: "delete this file"');
}

function healthCheck(filePath: string): HealthCheckResult {
    const issues: string[] = [];
    const score = 100;

    if (checkConsoleLogs(filePath)) {
        issues.push('Found console.log() in stdout');
    }

    if (checkDestructiveHint(filePath)) {
        issues.push('Missing destructiveHint annotation');
    }

    if (checkPromptInjection(filePath)) {
        issues.push('Prompt injection detected');
    }

    const grade = calculateGrade(score, issues.length);
    return { grade, score, issues };
}

function calculateGrade(score: number, issueCount: number): string {
    if (issueCount === 0) return 'A+';
    if (issueCount <= 2) return 'B';
    if (issueCount <= 4) return 'C';
    if (issueCount <= 6) return 'D';
    return 'F';
}

function main() {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.error('Usage: npx mcp-linter <path-to-your-server-code>');
        process.exit(1);
    }

    const filePath = args[0];
    if (!fs.existsSync(filePath)) {
        console.error(`File not found: ${filePath}`);
        process.exit(1);
    }

    const result = healthCheck(filePath);
    console.log(`Health Check Result for ${filePath}:`);
    console.log(`Grade: ${result.grade}`);
    console.log(`Score: ${result.score}`);
    console.log('Issues:');
    result.issues.forEach(issue => console.log(`- ${issue}`));
}

if (require.main === module) {
    main();
}